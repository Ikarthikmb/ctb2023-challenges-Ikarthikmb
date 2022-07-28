# Display of Instructions used in the Expected design
"""
print(("0000100" + "0".zfill(10) + "001" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--SHFL    53')
print(("0000100" + "0".zfill(10) + "100" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--PACK    41')
print(("0000100" + "0".zfill(10) + "101" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--UNSHFL  54')
print(("0000100" + "0".zfill(10) + "110" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--BEXT    40')
print(("0000100" + "0".zfill(10) + "111" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--PACKH   45')
print(("0000101" + "0".zfill(10) + "001" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--CLMUL   32')
print(("0000101" + "0".zfill(10) + "010" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--CLMULR  34')
print(("0000101" + "0".zfill(10) + "011" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--CLMULH  33')
print(("0000101" + "0".zfill(10) + "100" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--MIN     35')
print(("0000101" + "0".zfill(10) + "101" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--MAX     36')
print(("0000101" + "0".zfill(10) + "110" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--MINU    37')
print(("0000101" + "0".zfill(10) + "111" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--MAXU    38')
print(("0010000" + "0".zfill(10) + "001" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--SLO     4')
print(("0010000" + "0".zfill(10) + "010" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--SH1ADD  8')
print(("0010000" + "0".zfill(10) + "100" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--SH2ADD  9')
print(("0010000" + "0".zfill(10) + "101" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--SRO     5')
print(("0010000" + "0".zfill(10) + "110" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--SH3ADD  10')
print(("0010100" + "0".zfill(10) + "001" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--SBSET   12')
print(("0010100" + "0".zfill(10) + "101" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--GORC    15')
print(("0100000" + "0".zfill(10) + "100" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--XNOR    3')
print(("0100000" + "0".zfill(10) + "110" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--ORN     2')
print(("0100000" + "0".zfill(10) + "111" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--ANDN  1')
print(("0100100" + "0".zfill(10) + "001" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--SBCLR   11')
print(("0100100" + "0".zfill(10) + "100" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--PACKU   42')
print(("0100100" + "0".zfill(10) + "101" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--SBEXT   14')
print(("0100100" + "0".zfill(10) + "110" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--BDEP    39')
print(("0100100" + "0".zfill(10) + "111" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--BFP     60')
print(("0110000" + "0".zfill(10) + "001" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--ROL     6')
print(("0110000" + "0".zfill(10) + "101" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--ROR     7')
print(("0110100" + "0".zfill(10) + "001" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--SBINV  13')
print(("0110100" + "0".zfill(10) + "101" + "0".zfill(5) + "0110011" ).zfill(32)) # ('--GREV  16 (should check)')
print(("0110000" + "00000" + "001" + "0".zfill(5) + "0010011").zfill(32))	# ('--CLZ   21')
print(("0110000" + "00001" + "001" + "0".zfill(5) + "0010011").zfill(32))	# ('--CTZ    22')
print(("0110000" + "00010" + "001" + "0".zfill(5) + "0010011").zfill(32))	# ('--PCNT   23')
print(("0110000" + "00100" + "001" + "0".zfill(5) + "0010011").zfill(32))	# ('--SEXT.B  24')
print(("0110000" + "00101" + "001" + "0".zfill(5) + "0010011").zfill(32))	# ('--SEXT.H  25')
print(("0110000" + "10000" + "001" + "0".zfill(5) + "0010011").zfill(32))	# ('--CRC32.B 26')
print(("0110000" + "10001" + "001" + "0".zfill(5) + "0010011").zfill(32))	# ('--CRC32.H  27')
print(("0110000" + "10010" + "001" + "0".zfill(5) + "0010011").zfill(32))	# ('--CRC32.W  28')
print(("0110000" + "11000" + "001" + "0".zfill(5) + "0010011").zfill(32))	# ('--CRC32C.B 29')
print(("0110000" + "11001" + "001" + "0".zfill(5) + "0010011").zfill(32))	# ('--CRC32C.H  30')
print(("0110000" + "11010" + "001" + "0".zfill(5) + "0010011").zfill(32))	# ('--CRC32C.W  31')
print(("0".zfill(5) + "10" + "0".zfill(10) + "001" + "0".zfill(5) + "0110011").zfill(32)) # ('--FSL 19')
print(("0".zfill(5) + "10" + "0".zfill(10) + "101" + "0".zfill(5) + "0110011").zfill(32)) # ('--FSR  20(check)')
print(("0".zfill(5) + "11" + "0".zfill(10) + "001" + "0".zfill(5) + "0110011").zfill(32)) # ('--CMIX  17')
print(("0".zfill(5) + "11" + "0".zfill(10) + "101" + "0".zfill(5) + "0110011").zfill(32)) # ('--CMOV 18')
print(("0".zfill(5) + "1" + "0".zfill(11) + "101" + "0".zfill(5) + "0010011").zfill(32)) # ('--_FSRIs59')
print(("00100" + "0" + "0".zfill(11) + "101" + "0".zfill(5) + "0010011").zfill(32)) # ('--SROI 47')
print(("00101" + "0" + "0".zfill(11) + "101" + "0".zfill(5) + "0010011").zfill(32)) # ('--GORCI 57')
print(("01100" + "0" + "0".zfill(11) + "101" + "0".zfill(5) + "0010011").zfill(32)) # ('--RORIs48')
print(("01101" + "0" + "0".zfill(11) + "101" + "0".zfill(5) + "0010011").zfill(32)) # ('--GREVIs58')
print(("00100" + "0".zfill(12) + "001" + "0".zfill(5) + "0010011").zfill(32)) # ('--SLOIs46')
print(("00101" + "0".zfill(12) + "001" + "0".zfill(5) + "0010011").zfill(32)) # ('--SBSETIs 50')
print(("01001" + "0".zfill(12) + "001" + "0".zfill(5) + "0010011").zfill(32)) # ('--SBCLRIs 49')
print(("01001" + "0".zfill(12) + "101" + "0".zfill(5) + "0010011").zfill(32)) # ('--SBEXTIs52')
print(("01101" + "0".zfill(12) + "001" + "0".zfill(5) + "0010011").zfill(32)) # ('--SBINVIs51')
print(("000010" + "0".zfill(11) + "001" + "0".zfill(5) + "0010011").zfill(32)) # ('--SHFLIs55 (check)')
print(("000010" + "0".zfill(11) + "101" + "0".zfill(5) + "0010011").zfill(32)) # ('--UNSHFLIs56s(check)')
"""

print(("0".zfill(5) + "1" + "0".zfill(11) + "101" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--_FSRIs59')
print(("0".zfill(5) + "10" + "0".zfill(10) + "001" + "0".zfill(5) + "0110011").zfill(32), "INSTR:" '--FSL 19')
print(("0".zfill(5) + "10" + "0".zfill(10) + "101" + "0".zfill(5) + "0110011").zfill(32), "INSTR:" '--FSR  20(check)')
print(("0".zfill(5) + "11" + "0".zfill(10) + "001" + "0".zfill(5) + "0110011").zfill(32), "INSTR:" '--CMIX  17')
print(("0".zfill(5) + "11" + "0".zfill(10) + "101" + "0".zfill(5) + "0110011").zfill(32), "INSTR:" '--CMOV 18')
print(("000010" + "0".zfill(11) + "001" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--SHFLIs55 (check)')
print(("000010" + "0".zfill(11) + "101" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--UNSHFLIs56s(check)')
print(("0000100" + "0".zfill(10) + "001" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--SHFL    53')
print(("0000100" + "0".zfill(10) + "100" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--PACK    41')
print(("0000100" + "0".zfill(10) + "101" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--UNSHFL  54')
print(("0000100" + "0".zfill(10) + "110" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--BEXT    40')
print(("0000100" + "0".zfill(10) + "111" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--PACKH   45')
print(("0000101" + "0".zfill(10) + "001" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--CLMUL   32')
print(("0000101" + "0".zfill(10) + "010" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--CLMULR  34')
print(("0000101" + "0".zfill(10) + "011" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--CLMULH  33')
print(("0000101" + "0".zfill(10) + "100" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--MIN     35')
print(("0000101" + "0".zfill(10) + "101" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--MAX     36')
print(("0000101" + "0".zfill(10) + "110" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--MINU    37')
print(("0000101" + "0".zfill(10) + "111" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--MAXU    38')
print(("00100" + "0" + "0".zfill(11) + "101" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--SROI 47')
print(("00100" + "0".zfill(12) + "001" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--SLOIs46')
print(("0010000" + "0".zfill(10) + "001" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--SLO     4')
print(("0010000" + "0".zfill(10) + "010" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--SH1ADD  8')
print(("0010000" + "0".zfill(10) + "100" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--SH2ADD  9')
print(("0010000" + "0".zfill(10) + "101" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--SRO     5')
print(("0010000" + "0".zfill(10) + "110" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--SH3ADD  10')
print(("00101" + "0" + "0".zfill(11) + "101" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--GORCI 57')
print(("00101" + "0".zfill(12) + "001" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--SBSETIs 50')
print(("0010100" + "0".zfill(10) + "001" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--SBSET   12')
print(("0010100" + "0".zfill(10) + "101" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--GORC    15')
print(("0100000" + "0".zfill(10) + "100" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--XNOR    3')
print(("0100000" + "0".zfill(10) + "110" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--ORN     2')
print(("0100000" + "0".zfill(10) + "111" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--ANDN  1')
print(("01001" + "0".zfill(12) + "001" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--SBCLRIs 49')
print(("01001" + "0".zfill(12) + "101" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--SBEXTIs52')
print(("0100100" + "0".zfill(10) + "001" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--SBCLR   11')
print(("0100100" + "0".zfill(10) + "100" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--PACKU   42')
print(("0100100" + "0".zfill(10) + "101" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--SBEXT   14')
print(("0100100" + "0".zfill(10) + "110" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--BDEP    39')
print(("0100100" + "0".zfill(10) + "111" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--BFP     60')
print(("01100" + "0" + "0".zfill(11) + "101" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--RORIs48')
print(("0110000" + "0".zfill(10) + "001" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--ROL     6')
print(("0110000" + "0".zfill(10) + "101" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--ROR     7')
print(("0110000" + "00000" + "0".zfill(5) + "001" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--CLZ   21')
print(("0110000" + "00001" + "0".zfill(5) + "001" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--CTZ    22')
print(("0110000" + "00010" + "0".zfill(5) + "001" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--PCNT   23')
print(("0110000" + "00100" + "0".zfill(5) + "001" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--SEXT.B  24')
print(("0110000" + "00101" + "0".zfill(5) + "001" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--SEXT.H  25')
print(("0110000" + "10000" + "0".zfill(5) + "001" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--CRC32.B 26')
print(("0110000" + "10001" + "0".zfill(5) + "001" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--CRC32.H  27')
print(("0110000" + "10010" + "0".zfill(5) + "001" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--CRC32.W  28')
print(("0110000" + "11000" + "0".zfill(5) + "001" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--CRC32C.B 29')
print(("0110000" + "11001" + "0".zfill(5) + "001" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--CRC32C.H  30')
print(("0110000" + "11010" + "0".zfill(5) + "001" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--CRC32C.W  31')
print(("01101" + "0" + "0".zfill(11) + "101" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--GREVIs58')
print(("01101" + "0".zfill(12) + "001" + "0".zfill(5) + "0010011").zfill(32), "INSTR:" '--SBINVIs51')
print(("0110100" + "0".zfill(10) + "001" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--SBINV  13')
print(("0110100" + "0".zfill(10) + "101" + "0".zfill(5) + "0110011" ).zfill(32), "INSTR:" '--GREV  16 (should check)')
