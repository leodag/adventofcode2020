# copied from 01 as base
defmodule Aoc do
  def read_list(file) do
    File.stream!(file)
    |> Stream.map(&String.trim/1)
  end

  def search(_list, target, _, _) when target < 0, do: :notfound
  def search(_list, 0, 0, _), do: {:found, []}
  def search(_list, _, 0, _), do: :notfound
  def search([], _, _, _), do: :notfound

  def search(_list, target, 1, set) do
    if MapSet.member?(set, target) do
      {:found, [target]}
    else
      :notfound
    end
  end

  def search([head | rest], target, depth, set) do
    case search(rest, target - head, depth - 1, set) do
      {:found, members} ->
        {:found, [head | members]}
      :notfound ->
        search(rest, target, depth, set)
    end
  end

  def search(list, target, depth) do
    search(list, target, depth, MapSet.new(list))
  end

  def all_lists(list, partial \\ [])
  def all_lists([], partial) do
    partial
  end
  def all_lists(list = [_ | rest], partial) do
    all_lists(rest, [list | partial])
  end

  def part1(file \\ "input", preamble_len \\ 25) do
    {preamble, rest} =
      read_list(file)
      |> Stream.map(&String.to_integer/1)
      |> Enum.split(preamble_len)

    number =
      Enum.reduce_while(rest, preamble, fn n, prev = [_ | rest] ->
        case search(prev, n, 2) do
          {:found, _} ->
            {:cont, rest ++ [n]}
          :notfound ->
            {:halt, n}
        end
      end)

    IO.puts(number)
  end

  def do_search_consec(_list, target) when target < 0, do: :notfound
  def do_search_consec(_list, 0), do: {:found, []}
  def do_search_consec([], _), do: :notfound

  def do_search_consec([head | rest], target) do
    case do_search_consec(rest, target - head) do
      {:found, members} ->
        {:found, [head | members]}
      :notfound ->
        :notfound
    end
  end

  def search_consec(list = [_ | rest], target) do
    case do_search_consec(list, target) do
      {:found, members} ->
        {:found, members}
      :notfound ->
        search_consec(rest, target)
    end
  end

  def part2(file \\ "input", preamble_len \\ 25) do
    numbers =
      read_list(file)
      |> Enum.map(&String.to_integer/1)

    {preamble, rest} =
      numbers
      |> Enum.split(preamble_len)

    number =
      Enum.reduce_while(rest, preamble, fn n, prev = [_ | rest] ->
        case search(prev, n, 2) do
          {:found, _} ->
            {:cont, rest ++ [n]}
          :notfound ->
            {:halt, n}
        end
      end)

    {:found, sum_numbers} = search_consec(numbers, number)

    IO.puts(Enum.max(sum_numbers) + Enum.min(sum_numbers))
  end
end
