#!/usr/bin/env elixir

defmodule Aoc do
  def list, do: [1721, 979, 366, 299, 675]

  def read_list() do
    IO.stream(:stdio, :line)
    |> Stream.map(&String.trim/1)
    |> Stream.map(&String.to_integer/1)
    |> Enum.to_list()
  end

  def read_list(file) do
    File.stream!(file)
    |> Stream.map(&String.trim/1)
    |> Stream.map(&String.to_integer/1)
    |> Enum.to_list()
  end

  def search(_list, target, _) when target < 0, do: :notfound
  def search(_list, 0, 0), do: {:found, []}
  def search(_list, _, 0), do: :notfound
  def search([], _, _), do: :notfound

  def search([head | rest], target, depth) do
    case search(rest, target - head, depth - 1) do
      {:found, members} ->
        {:found, [head | members]}
      :notfound ->
        search(rest, target, depth)
    end
  end

  def do_search2(_list, target, _, _) when target < 0, do: :notfound
  def do_search2(_list, 0, 0, _), do: {:found, []}
  def do_search2(_list, _, 0, _), do: :notfound
  def do_search2([], _, _, _), do: :notfound

  def do_search2(_list, target, 1, set) do
    if MapSet.member?(set, target) do
      {:found, [target]}
    else
      :notfound
    end
  end

  def do_search2([head | rest], target, depth, set) do
    case do_search2(rest, target - head, depth - 1, set) do
      {:found, members} ->
        {:found, [head | members]}
      :notfound ->
        do_search2(rest, target, depth, set)
    end
  end

  def search2(list, target, depth) do
    do_search2(list, target, depth, MapSet.new(list))
  end

  def part1() do
    {:found, numbers} =
      read_list("input")
      |> search2(2020, 2)

    numbers
    |> Enum.reduce(1, &(&1 * &2))
    |> IO.puts()
  end

  def part2() do
    {:found, numbers} =
      read_list("input")
      |> search2(2020, 3)

    numbers
    |> Enum.reduce(1, &(&1 * &2))
    |> IO.puts()
  end
end
