from graphs.use_cases.adjacency_structure_use_cases.DeepSearchUseCaseAdjacency import DeepSearchUseCaseAdjacency
from graphs.use_cases.adjacency_structure_use_cases.SubgraphUseCaseAdjacency import SubgraphUseCaseAdjacency
from graphs.use_cases.matrix_use_cases.CompleteGraphUseCaseMatrix import CompleteGraphUseCaseMatrix
from graphs.use_cases.matrix_use_cases.BasicFirstUseCaseMatrix import BasicFirstUseCaseMatrix
from graphs.use_cases.matrix_use_cases.BasicSecondUseCaseMatrix import BasicSecondUseCaseMatrix
from graphs.use_cases.adjacency_structure_use_cases.BasicFirstUseCaseAdjacency import BasicFirstUseCaseAdjacency
from graphs.use_cases.adjacency_structure_use_cases.BasicSecondUseCaseAdjacency import BasicSecondUseCaseAdjacency

use_case_01 = BasicFirstUseCaseMatrix()
print()
use_case_02 = BasicSecondUseCaseMatrix()
print()
use_case_03 = BasicFirstUseCaseAdjacency()
print()
use_case_04 = BasicSecondUseCaseAdjacency()
print()
use_case_05 = CompleteGraphUseCaseMatrix()
print("EXEMPLO BUSCA EM PROFUNDIDADE")
use_case_06 = DeepSearchUseCaseAdjacency()
print()
use_case_07 = SubgraphUseCaseAdjacency()



