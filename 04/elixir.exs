defmodule Aoc do
  def read_list(file) do
    File.stream!(file)
    |> Stream.map(&String.trim/1)
  end

  def chunk_by_empty_line(stream) do
    chunk_fun = fn element, acc ->
      if element == "" do
        {:cont, acc, []}
      else
        {:cont, [element | acc]}
      end
    end

    after_fun = fn
      [] -> {:cont, []}
      acc -> {:cont, acc, []}
    end

    stream
    |> Stream.chunk_while([], chunk_fun, after_fun)
  end

  def separate_fields(line, separator \\ " ") do
    line
    |> String.split(separator)
  end

  def read_passport(lines) do
    lines
    # separate fields in each line
    |> Enum.map(&separate_fields/1)
    # join lines in a flat list
    |> List.flatten()
    |> Enum.map(fn field ->
      field
      |> String.split(":")
      |> List.to_tuple()
    end)
    |> Map.new()
  end

  @required_keys ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
  def validate_passport(passport) do
    @required_keys
    |> Enum.all?(&(Map.has_key?(passport, &1)))
  end

  def part1(file \\ "input") do
    read_list(file)
    |> chunk_by_empty_line()
    |> Stream.map(&read_passport/1)
    |> Stream.map(&validate_passport/1)
    |> Enum.count(&Function.identity/1)
  end

  @valid_eye_colors ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
  @required_keys2 %{
    "byr" => {:length_and_range, 4, 1920, 2002},
    "iyr" => {:length_and_range, 4, 2010, 2020},
    "eyr" => {:length_and_range, 4, 2020, 2030},
    "hgt" => &Aoc.validate_height/1,
    "hcl" => ~r/^#[0-9a-f]{6}$/i,
    "ecl" => @valid_eye_colors,
    "pid" => ~r/^\d{9}$/,
  }

  def validate_height(value) do
    case Integer.parse(value) do
      {val, "cm"} ->
        150 <= val and val <= 193
      {val, "in"} ->
        59 <= val and val <= 76
      _ ->
        false
    end
  end

  def validate_length_and_range(value, length, min, max) do
    case Integer.parse(value) do
      {val, _rest} ->
        String.length(value) == length and min <= val and val <= max
      :error ->
        false
      _ ->
        raise "weird"
    end
  end

  def apply_validator(value, {:length_and_range, length, min, max}) do
    validate_length_and_range(value, length, min, max)
  end

  def apply_validator(value, validator) when is_list(validator) do
    value in validator
  end

  def apply_validator(value, validator) when is_function(validator) do
    validator.(value)
  end

  def apply_validator(value, validator) when is_struct(validator, Regex) do
    Regex.match?(validator, value)
  end

  def validate_passport2(passport) do
    @required_keys2
    |> Enum.map(fn {key, validator} ->
      case Map.get(passport, key) do
        val when not is_nil(val) ->
          apply_validator(val, validator)
        _ ->
          false
      end
    end)
    |> Enum.all?()
  end

  def part2(file \\ "input") do
        read_list(file)
    |> chunk_by_empty_line()
    |> Stream.map(&read_passport/1)
    |> Stream.map(&validate_passport2/1)
    |> Enum.count(&Function.identity/1)
  end
end
