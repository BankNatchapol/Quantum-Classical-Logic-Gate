from qiskit import *
import warnings
warnings.filterwarnings("ignore")
import logging
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})
def not_gate(bit, backend='sim', token=None):
    assert bit in (0, 1), "Only 0 or 1"
    quantumBits = 1
    classicalBits = 1
    NOT = QuantumCircuit(quantumBits, classicalBits)

    if bit == 1:
        NOT.x(0)
    NOT.barrier()

    NOT.x(0)

    NOT.barrier()
    NOT.measure([0], [0])

    if backend == 'sim':
        sim = Aer.get_backend('qasm_simulator')
        result = execute(NOT, backend=sim, shots=1).result()

    elif backend == 'real':
        IBMQ.delete_account()
        IBMQ.save_account(token, overwrite=True)
        IBMQ.load_account()
        # execute on real quantum computer
        provider = IBMQ.get_provider('ibm-q')
        qcomp = provider.get_backend('ibmq_16_melbourne')
        job = execute(NOT, backend=qcomp)
        result = job.result()  # get result from real quantum computer

    counts = result.get_counts()
    value = max(counts, key=counts.get)
    return value


def and_gate(bit1, bit2, backend='sim', token=None):
    assert bit1 in (0, 1) and bit2 in (0, 1), "Only 0 or 1"
    quantumBits = 3
    classicalBits = 1
    AND = QuantumCircuit(quantumBits, classicalBits)

    if bit1 == 1:
        AND.x(0)
    if bit2 == 1:
        AND.x(1)
    AND.barrier()

    AND.ccx(0, 1, 2)

    AND.barrier()
    AND.measure([2], [0])

    if backend == 'sim':
        sim = Aer.get_backend('qasm_simulator')
        result = execute(AND, backend=sim, shots=1).result()

    elif backend == 'real':
        IBMQ.delete_account()
        IBMQ.save_account(token, overwrite=True)
        IBMQ.load_account()
        # execute on real quantum computer
        provider = IBMQ.get_provider('ibm-q')
        qcomp = provider.get_backend('ibmq_16_melbourne')
        job = execute(AND, backend=qcomp)
        result = job.result()  # get result from real quantum computer

    counts = result.get_counts()
    value = max(counts, key=counts.get)
    return value


def or_gate(bit1, bit2, backend='sim', token=None):
    assert bit1 in (0, 1) and bit2 in (0, 1), "Only 0 or 1"
    quantumBits = 3
    classicalBits = 1
    OR = QuantumCircuit(quantumBits, classicalBits)

    if bit1 == 1:
        OR.x(0)
    if bit2 == 1:
        OR.x(1)
    OR.barrier()

    OR.x(0)
    OR.x(1)
    OR.x(2)
    OR.ccx(0, 1, 2)
    OR.x(0)
    OR.x(1)

    OR.barrier()
    OR.measure([2], [0])

    if backend == 'sim':
        sim = Aer.get_backend('qasm_simulator')
        result = execute(OR, backend=sim, shots=1).result()

    elif backend == 'real':
        IBMQ.delete_account()
        IBMQ.save_account(token, overwrite=True)
        IBMQ.load_account()
        # execute on real quantum computer
        provider = IBMQ.get_provider('ibm-q')
        qcomp = provider.get_backend('ibmq_16_melbourne')
        job = execute(OR, backend=qcomp)
        result = job.result()  # get result from real quantum computer

    counts = result.get_counts()
    value = max(counts, key=counts.get)
    return value


def xor_gate(bit1, bit2, backend='sim', token=None):
    assert bit1 in (0, 1) and bit2 in (0, 1), "Only 0 or 1"
    quantumBits = 2
    classicalBits = 1
    XOR = QuantumCircuit(quantumBits, classicalBits)

    if bit1 == 1:
        XOR.x(0)
    if bit2 == 1:
        XOR.x(1)
    XOR.barrier()

    XOR.cx(0, 1)

    XOR.barrier()
    XOR.measure([1], [0])

    if backend == 'sim':
        sim = Aer.get_backend('qasm_simulator')
        result = execute(XOR, backend=sim, shots=1).result()

    elif backend == 'real':
        IBMQ.delete_account()
        IBMQ.save_account(token, overwrite=True)
        IBMQ.load_account()
        # execute on real quantum computer
        provider = IBMQ.get_provider('ibm-q')
        qcomp = provider.get_backend('ibmq_16_melbourne')
        job = execute(XOR, backend=qcomp)
        result = job.result()  # get result from real quantum computer

    counts = result.get_counts()
    value = max(counts, key=counts.get)
    return value
