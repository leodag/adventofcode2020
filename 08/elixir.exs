defmodule Aoc do
  defmodule State do
    defstruct acc: 0, ip: 0, ir: nil, visited: MapSet.new(), memory: []
  end

  def read_lines(file) do
    File.stream!(file)
    |> Stream.map(&String.trim/1)
  end

  def parse_instruction(line) do
    instruction =
      line
      |> String.split()
      |> List.to_tuple()

    arg =
      instruction
      |> elem(1)
      |> String.to_integer()

    put_elem(instruction, 1, arg)
  end

  def parse_instructions(lines) do
    lines
    |> Enum.map(&parse_instruction/1)
    |> List.to_tuple()
  end

  def run_instruction(state = %State{ir: {"acc", arg}, acc: acc}) do
    %State{state | acc: acc + arg}
  end

  def run_instruction(state = %State{ir: {"jmp", arg}, ip: ip}) do
    %State{state | ip: ip + arg - 1}
  end

  def run_instruction(state = %State{ir: {"nop", _arg}}) do
    state
  end

  def increment_ip(state = %State{visited: visited, ip: ip}) do
    %State{
      state
      | visited: MapSet.put(visited, ip),
        ip: ip + 1
    }
  end

  def run_cycle(state = %State{ip: ip, memory: memory}) do
    instruction = elem(memory, ip)

    %State{state | ir: instruction}
    |> run_instruction()
    |> increment_ip()
  end

  def run_program(state \\ %State{})

  def run_program(%State{acc: acc, ip: ip, memory: mem}) when ip == tuple_size(mem) do
    {ip, acc}
  end

  def run_program(state = %State{acc: acc, ip: ip, visited: visited}) do
    case ip in visited do
      false ->
        run_cycle(state)
        |> run_program()

      true ->
        {ip, acc}
    end
  end

  def part1(file \\ "input") do
    memory =
      read_lines(file)
      |> parse_instructions()

    {_ip, acc} = run_program(%State{memory: memory})
    acc
  end

  def mutated(instructions, addr) do
    put_elem(instructions, addr, {"nop", 0})
  end

  def mutations(instructions) do
    0..(tuple_size(instructions) - 1)
    |> Enum.filter(fn addr -> instructions |> elem(addr) |> elem(0) == "jmp" end)
    |> Stream.map(fn addr -> mutated(instructions, addr) end)
  end

  def part2(file \\ "input") do
    original =
      read_lines(file)
      |> parse_instructions()

    {_ip, acc} =
      mutations(original)
      |> Stream.map(fn instr ->
        run_program(%State{memory: instr})
      end)
      |> Enum.find(fn {ip, _acc} ->
        ip == tuple_size(original)
      end)

    acc
  end
end
