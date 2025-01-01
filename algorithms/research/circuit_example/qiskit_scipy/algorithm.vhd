library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Quantum_Algorithm is
    Port ( a : in STD_LOGIC;
           b : in STD_LOGIC;
           cin : in STD_LOGIC;
           sum : out STD_LOGIC;
           cout : out STD_LOGIC);
end Quantum_Algorithm;

architecture Behavioral of Quantum_Algorithm is
component HalfAdder is
    Port ( a : in STD_LOGIC;
           b : in STD_LOGIC;
           s : out STD_LOGIC;
           c : out STD_LOGIC);
end component;

signal s1, c1, c2: std_logic;

begin
    -- Algorithm(1)
    HA1: HalfAdder port map (a, b, s1, c1);
    HA2: HalfAdder port map (s1, cin, sum, c2);
    cout <= c1 or c2;

    -- Algorithm(2)
    HA1_2: HalfAdder port map (a, b, s1, c1);
    HA2_2: HalfAdder port map (s1, cin, sum, c2);
    cout <= c1 or c2;

    -- Algorithm(3)
    HA1_3: HalfAdder port map (a, b, s1, c1);
    HA2_3: HalfAdder port map (s1, cin, sum, c2);
    cout <= c1 or c2;

end Behavioral;
