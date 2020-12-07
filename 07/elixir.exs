defmodule Aoc do
  def read_list(file) do
    File.stream!(file)
    |> Stream.map(&String.trim/1)
  end

  def parse_bag_amount_and_name(amount_and_name) do
    [amount, name] = String.split(amount_and_name, " ", parts: 2)
    {String.to_integer(amount), parse_bag_name(name)}
  end

  def parse_bag_name(name) do
    String.replace(name, ~r/ bags?$/, "")
  end

  def parse_right_bags("no other bags"), do: []

  def parse_right_bags(right_bags) do
    right_bags
    |> String.split(", ")
    |> Enum.map(&parse_bag_amount_and_name/1)
  end

  def parse_line(line) do
    [left_bag, right_bags] =
      line
      |> String.replace_suffix(".", "")
      |> String.split(" contain ")

    {parse_bag_name(left_bag), parse_right_bags(right_bags)}
  end

  def contained_map(bag_rules) do
    Enum.reduce(bag_rules, %{}, fn {left_bag, right_bags}, map ->
      Enum.reduce(right_bags, map, fn {amount, right_bag}, map ->
        put_in(
          map,
          [Access.key(right_bag, %{}), left_bag],
          amount
        )
      end)
    end)
  end

  def contains_map(bag_rules) do
    Enum.reduce(bag_rules, %{}, fn {left_bag, right_bags}, map ->
      Enum.reduce(right_bags, map, fn {amount, right_bag}, map ->
        put_in(
          map,
          [Access.key(left_bag, %{}), right_bag],
          amount
        )
      end)
    end)
  end

  def can_contain(contained_map, bag, can_contain_set \\ MapSet.new()) do
    contained_map
    |> Map.get(bag, %{})
    |> Enum.reduce(can_contain_set, fn {container, _amt}, set ->
      if MapSet.member?(can_contain_set, container) do
        set
      else
        set = MapSet.put(set, container)
        can_contain(contained_map, container, set)
      end
    end)
  end

  def part1() do
    read_list("input")
    |> Stream.map(&parse_line/1)
    |> contained_map()
    |> can_contain("shiny gold")
    |> MapSet.size()
  end

  def total_contained(contains_map, bag) do
    contains_map
    |> Map.get(bag, %{})
    |> Enum.map(fn {bag, count} ->
      count * (1 + total_contained(contains_map, bag))
    end)
    |> Enum.sum()
  end

  def total_contained_memoized(contains_map, bag, memo \\ %{}) do
    contains_map
    |> Map.get(bag, %{})
    |> Enum.reduce({0, memo}, fn {bag, count}, {sum, memo} ->
      case Map.get(memo, bag) do
        nil ->
          {contained_single, memo} = total_contained_memoized(contains_map, bag, memo)
          addition = count * (1 + contained_single)
          {sum + addition, Map.put(memo, bag, contained_single)}
        val ->
          addition = count * (1 + val)
          {sum + addition, memo}
      end
    end)
  end

  def total_contained2(contains_map, bag) do
    {result, _memo} = total_contained_memoized(contains_map, bag)
    result
  end

  def part2() do
    read_list("input")
    |> Stream.map(&parse_line/1)
    |> contains_map()
    |> total_contained2("shiny gold")
  end
end
