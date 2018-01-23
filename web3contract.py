import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from web3.contract import ConciseContract

abi = json.loads("""
[
	{
		"constant": true,
		"inputs": [],
		"name": "patientId",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"name": "diagnosises",
		"outputs": [
			{
				"name": "fileHash",
				"type": "string"
			},
			{
				"name": "diagnosis",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "fileHash",
				"type": "string"
			},
			{
				"name": "diagnosis",
				"type": "string"
			}
		],
		"name": "addDiagnosis",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "patientId",
				"type": "string"
			}
		],
		"name": "setPatientInfo",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
""")

bytecode = """
{
	"linkReferences": {},
	"object": "6060604052341561000f57600080fd5b6106128061001e6000396000f300606060405260043610610062576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063873299d914610067578063a5be0065146101a9578063e07f444414610206578063ea40041814610294575b600080fd5b341561007257600080fd5b6100886004808035906020019091905050610334565b6040518080602001806020018381038352858181546001816001161561010002031660029004815260200191508054600181600116156101000203166002900480156101155780601f106100ea57610100808354040283529160200191610115565b820191906000526020600020905b8154815290600101906020018083116100f857829003601f168201915b50508381038252848181546001816001161561010002031660029004815260200191508054600181600116156101000203166002900480156101985780601f1061016d57610100808354040283529160200191610198565b820191906000526020600020905b81548152906001019060200180831161017b57829003601f168201915b505094505050505060405180910390f35b34156101b457600080fd5b610204600480803590602001908201803590602001908080601f01602080910402602001604051908101604052809392919081815260200183838082843782019150505050505091905050610365565b005b341561021157600080fd5b61021961036b565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561025957808201518184015260208101905061023e565b50505050905090810190601f1680156102865780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b341561029f57600080fd5b610332600480803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509190803590602001908201803590602001908080601f01602080910402602001604051908101604052809392919081815260200183838082843782019150505050505091905050610409565b005b60018181548110151561034357fe5b9060005260206000209060020201600091509050806000019080600101905082565b80905050565b60008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156104015780601f106103d657610100808354040283529160200191610401565b820191906000526020600020905b8154815290600101906020018083116103e457829003601f168201915b505050505081565b6001805480600101828161041d9190610488565b91600052602060002090600202016000604080519081016040528086815260200185815250909190915060008201518160000190805190602001906104639291906104ba565b5060208201518160010190805190602001906104809291906104ba565b505050505050565b8154818355818115116104b5576002028160020283600052602060002091820191016104b4919061053a565b5b505050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106104fb57805160ff1916838001178555610529565b82800160010185558215610529579182015b8281111561052857825182559160200191906001019061050d565b5b5090506105369190610579565b5090565b61057691905b808211156105725760008082016000610559919061059e565b600182016000610569919061059e565b50600201610540565b5090565b90565b61059b91905b8082111561059757600081600090555060010161057f565b5090565b90565b50805460018160011615610100020316600290046000825580601f106105c457506105e3565b601f0160209004906000526020600020908101906105e29190610579565b5b505600a165627a7a7230582085bf2464e3c27223271d06932bb05531e2aad0086308595ca2a4700cb0a5dde50029",
	"opcodes": "PUSH1 0x60 PUSH1 0x40 MSTORE CALLVALUE ISZERO PUSH2 0xF JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH2 0x612 DUP1 PUSH2 0x1E PUSH1 0x0 CODECOPY PUSH1 0x0 RETURN STOP PUSH1 0x60 PUSH1 0x40 MSTORE PUSH1 0x4 CALLDATASIZE LT PUSH2 0x62 JUMPI PUSH1 0x0 CALLDATALOAD PUSH29 0x100000000000000000000000000000000000000000000000000000000 SWAP1 DIV PUSH4 0xFFFFFFFF AND DUP1 PUSH4 0x873299D9 EQ PUSH2 0x67 JUMPI DUP1 PUSH4 0xA5BE0065 EQ PUSH2 0x1A9 JUMPI DUP1 PUSH4 0xE07F4444 EQ PUSH2 0x206 JUMPI DUP1 PUSH4 0xEA400418 EQ PUSH2 0x294 JUMPI JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST CALLVALUE ISZERO PUSH2 0x72 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH2 0x88 PUSH1 0x4 DUP1 DUP1 CALLDATALOAD SWAP1 PUSH1 0x20 ADD SWAP1 SWAP2 SWAP1 POP POP PUSH2 0x334 JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 DUP1 PUSH1 0x20 ADD DUP1 PUSH1 0x20 ADD DUP4 DUP2 SUB DUP4 MSTORE DUP6 DUP2 DUP2 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV DUP2 MSTORE PUSH1 0x20 ADD SWAP2 POP DUP1 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV DUP1 ISZERO PUSH2 0x115 JUMPI DUP1 PUSH1 0x1F LT PUSH2 0xEA JUMPI PUSH2 0x100 DUP1 DUP4 SLOAD DIV MUL DUP4 MSTORE SWAP2 PUSH1 0x20 ADD SWAP2 PUSH2 0x115 JUMP JUMPDEST DUP3 ADD SWAP2 SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 JUMPDEST DUP2 SLOAD DUP2 MSTORE SWAP1 PUSH1 0x1 ADD SWAP1 PUSH1 0x20 ADD DUP1 DUP4 GT PUSH2 0xF8 JUMPI DUP3 SWAP1 SUB PUSH1 0x1F AND DUP3 ADD SWAP2 JUMPDEST POP POP DUP4 DUP2 SUB DUP3 MSTORE DUP5 DUP2 DUP2 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV DUP2 MSTORE PUSH1 0x20 ADD SWAP2 POP DUP1 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV DUP1 ISZERO PUSH2 0x198 JUMPI DUP1 PUSH1 0x1F LT PUSH2 0x16D JUMPI PUSH2 0x100 DUP1 DUP4 SLOAD DIV MUL DUP4 MSTORE SWAP2 PUSH1 0x20 ADD SWAP2 PUSH2 0x198 JUMP JUMPDEST DUP3 ADD SWAP2 SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 JUMPDEST DUP2 SLOAD DUP2 MSTORE SWAP1 PUSH1 0x1 ADD SWAP1 PUSH1 0x20 ADD DUP1 DUP4 GT PUSH2 0x17B JUMPI DUP3 SWAP1 SUB PUSH1 0x1F AND DUP3 ADD SWAP2 JUMPDEST POP POP SWAP5 POP POP POP POP POP PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST CALLVALUE ISZERO PUSH2 0x1B4 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH2 0x204 PUSH1 0x4 DUP1 DUP1 CALLDATALOAD SWAP1 PUSH1 0x20 ADD SWAP1 DUP3 ADD DUP1 CALLDATALOAD SWAP1 PUSH1 0x20 ADD SWAP1 DUP1 DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP4 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP4 DUP4 DUP1 DUP3 DUP5 CALLDATACOPY DUP3 ADD SWAP2 POP POP POP POP POP POP SWAP2 SWAP1 POP POP PUSH2 0x365 JUMP JUMPDEST STOP JUMPDEST CALLVALUE ISZERO PUSH2 0x211 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH2 0x219 PUSH2 0x36B JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 DUP1 PUSH1 0x20 ADD DUP3 DUP2 SUB DUP3 MSTORE DUP4 DUP2 DUP2 MLOAD DUP2 MSTORE PUSH1 0x20 ADD SWAP2 POP DUP1 MLOAD SWAP1 PUSH1 0x20 ADD SWAP1 DUP1 DUP4 DUP4 PUSH1 0x0 JUMPDEST DUP4 DUP2 LT ISZERO PUSH2 0x259 JUMPI DUP1 DUP3 ADD MLOAD DUP2 DUP5 ADD MSTORE PUSH1 0x20 DUP2 ADD SWAP1 POP PUSH2 0x23E JUMP JUMPDEST POP POP POP POP SWAP1 POP SWAP1 DUP2 ADD SWAP1 PUSH1 0x1F AND DUP1 ISZERO PUSH2 0x286 JUMPI DUP1 DUP3 SUB DUP1 MLOAD PUSH1 0x1 DUP4 PUSH1 0x20 SUB PUSH2 0x100 EXP SUB NOT AND DUP2 MSTORE PUSH1 0x20 ADD SWAP2 POP JUMPDEST POP SWAP3 POP POP POP PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST CALLVALUE ISZERO PUSH2 0x29F JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH2 0x332 PUSH1 0x4 DUP1 DUP1 CALLDATALOAD SWAP1 PUSH1 0x20 ADD SWAP1 DUP3 ADD DUP1 CALLDATALOAD SWAP1 PUSH1 0x20 ADD SWAP1 DUP1 DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP4 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP4 DUP4 DUP1 DUP3 DUP5 CALLDATACOPY DUP3 ADD SWAP2 POP POP POP POP POP POP SWAP2 SWAP1 DUP1 CALLDATALOAD SWAP1 PUSH1 0x20 ADD SWAP1 DUP3 ADD DUP1 CALLDATALOAD SWAP1 PUSH1 0x20 ADD SWAP1 DUP1 DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP4 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP4 DUP4 DUP1 DUP3 DUP5 CALLDATACOPY DUP3 ADD SWAP2 POP POP POP POP POP POP SWAP2 SWAP1 POP POP PUSH2 0x409 JUMP JUMPDEST STOP JUMPDEST PUSH1 0x1 DUP2 DUP2 SLOAD DUP2 LT ISZERO ISZERO PUSH2 0x343 JUMPI INVALID JUMPDEST SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 PUSH1 0x2 MUL ADD PUSH1 0x0 SWAP2 POP SWAP1 POP DUP1 PUSH1 0x0 ADD SWAP1 DUP1 PUSH1 0x1 ADD SWAP1 POP DUP3 JUMP JUMPDEST DUP1 SWAP1 POP POP JUMP JUMPDEST PUSH1 0x0 DUP1 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP1 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV DUP1 ISZERO PUSH2 0x401 JUMPI DUP1 PUSH1 0x1F LT PUSH2 0x3D6 JUMPI PUSH2 0x100 DUP1 DUP4 SLOAD DIV MUL DUP4 MSTORE SWAP2 PUSH1 0x20 ADD SWAP2 PUSH2 0x401 JUMP JUMPDEST DUP3 ADD SWAP2 SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 JUMPDEST DUP2 SLOAD DUP2 MSTORE SWAP1 PUSH1 0x1 ADD SWAP1 PUSH1 0x20 ADD DUP1 DUP4 GT PUSH2 0x3E4 JUMPI DUP3 SWAP1 SUB PUSH1 0x1F AND DUP3 ADD SWAP2 JUMPDEST POP POP POP POP POP DUP2 JUMP JUMPDEST PUSH1 0x1 DUP1 SLOAD DUP1 PUSH1 0x1 ADD DUP3 DUP2 PUSH2 0x41D SWAP2 SWAP1 PUSH2 0x488 JUMP JUMPDEST SWAP2 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 PUSH1 0x2 MUL ADD PUSH1 0x0 PUSH1 0x40 DUP1 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 DUP7 DUP2 MSTORE PUSH1 0x20 ADD DUP6 DUP2 MSTORE POP SWAP1 SWAP2 SWAP1 SWAP2 POP PUSH1 0x0 DUP3 ADD MLOAD DUP2 PUSH1 0x0 ADD SWAP1 DUP1 MLOAD SWAP1 PUSH1 0x20 ADD SWAP1 PUSH2 0x463 SWAP3 SWAP2 SWAP1 PUSH2 0x4BA JUMP JUMPDEST POP PUSH1 0x20 DUP3 ADD MLOAD DUP2 PUSH1 0x1 ADD SWAP1 DUP1 MLOAD SWAP1 PUSH1 0x20 ADD SWAP1 PUSH2 0x480 SWAP3 SWAP2 SWAP1 PUSH2 0x4BA JUMP JUMPDEST POP POP POP POP POP POP JUMP JUMPDEST DUP2 SLOAD DUP2 DUP4 SSTORE DUP2 DUP2 ISZERO GT PUSH2 0x4B5 JUMPI PUSH1 0x2 MUL DUP2 PUSH1 0x2 MUL DUP4 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP2 DUP3 ADD SWAP2 ADD PUSH2 0x4B4 SWAP2 SWAP1 PUSH2 0x53A JUMP JUMPDEST JUMPDEST POP POP POP JUMP JUMPDEST DUP3 DUP1 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 PUSH1 0x1F ADD PUSH1 0x20 SWAP1 DIV DUP2 ADD SWAP3 DUP3 PUSH1 0x1F LT PUSH2 0x4FB JUMPI DUP1 MLOAD PUSH1 0xFF NOT AND DUP4 DUP1 ADD OR DUP6 SSTORE PUSH2 0x529 JUMP JUMPDEST DUP3 DUP1 ADD PUSH1 0x1 ADD DUP6 SSTORE DUP3 ISZERO PUSH2 0x529 JUMPI SWAP2 DUP3 ADD JUMPDEST DUP3 DUP2 GT ISZERO PUSH2 0x528 JUMPI DUP3 MLOAD DUP3 SSTORE SWAP2 PUSH1 0x20 ADD SWAP2 SWAP1 PUSH1 0x1 ADD SWAP1 PUSH2 0x50D JUMP JUMPDEST JUMPDEST POP SWAP1 POP PUSH2 0x536 SWAP2 SWAP1 PUSH2 0x579 JUMP JUMPDEST POP SWAP1 JUMP JUMPDEST PUSH2 0x576 SWAP2 SWAP1 JUMPDEST DUP1 DUP3 GT ISZERO PUSH2 0x572 JUMPI PUSH1 0x0 DUP1 DUP3 ADD PUSH1 0x0 PUSH2 0x559 SWAP2 SWAP1 PUSH2 0x59E JUMP JUMPDEST PUSH1 0x1 DUP3 ADD PUSH1 0x0 PUSH2 0x569 SWAP2 SWAP1 PUSH2 0x59E JUMP JUMPDEST POP PUSH1 0x2 ADD PUSH2 0x540 JUMP JUMPDEST POP SWAP1 JUMP JUMPDEST SWAP1 JUMP JUMPDEST PUSH2 0x59B SWAP2 SWAP1 JUMPDEST DUP1 DUP3 GT ISZERO PUSH2 0x597 JUMPI PUSH1 0x0 DUP2 PUSH1 0x0 SWAP1 SSTORE POP PUSH1 0x1 ADD PUSH2 0x57F JUMP JUMPDEST POP SWAP1 JUMP JUMPDEST SWAP1 JUMP JUMPDEST POP DUP1 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV PUSH1 0x0 DUP3 SSTORE DUP1 PUSH1 0x1F LT PUSH2 0x5C4 JUMPI POP PUSH2 0x5E3 JUMP JUMPDEST PUSH1 0x1F ADD PUSH1 0x20 SWAP1 DIV SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 DUP2 ADD SWAP1 PUSH2 0x5E2 SWAP2 SWAP1 PUSH2 0x579 JUMP JUMPDEST JUMPDEST POP JUMP STOP LOG1 PUSH6 0x627A7A723058 KECCAK256 DUP6 0xbf 0x24 PUSH5 0xE3C2722327 0x1d MOD SWAP4 0x2b 0xb0 SSTORE BALANCE 0xe2 0xaa 0xd0 ADDMOD PUSH4 0x8595CA2 LOG4 PUSH17 0xCB0A5DDE5002900000000000000000000 ",
	"sourceMap": "0:403:0:-;;;;;;;;;;;;;;;;;"
}
"""


web3prov = Web3(HTTPProvider('https://ropsten.infura.io'))
my_account = "0x0fC1A83F77FA3C9f53dbA8B439D861faA35fE315"
my_password = "titok123"
my_private_key = "1e10130053d9528dd059706a8e8ff7cdea373c4b3437f9b0e66d8d68bcf6b528"
contractAddress = "0xccf510c7e770bce34345fc519795be9b6eee41cb"
contract = web3prov.eth.contract(abi=abi, address=contractAddress, ContractFactoryClass=ConciseContract)
#print(contract)
print(web3prov.eth.account)
print(contract.functions)
transaction = contract.functions.addDiagnosis('filehash1', 'Diag1')
print(transaction)
#signed = web3prov.eth.account.signTransaction(transaction, my_private_key)
#web3prov.eth.sendRawTransaction(signed.rawTransaction)
# add new string here
#print(contract.addDiagnosis('filehash1', 'Diag1', transact={'from': web3prov.eth.accounts[0]}))
print('result string', contract.diagnosises(0))

