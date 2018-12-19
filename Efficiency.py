import math
# all values will be for little boy bomb with uranium core an Tungsten-carbide Tamper:
# define constants for later use:


def efficiency():

    m_neutron = 1.674927 * 10 ** (- 27)  # neutron mass in kg
    NA = 6.022142 * 10 ** 23  # Avogadro's number
    pi = math.pi
    ep = 1.6021765 * 10 ** -13  # joule/MeV
    E_neutron = 2  # energy of neutron in MeV
    v_neutron = 1.956083 * 10 ** 9  # neutron velocity in cm/s
    kt = 4.2 * 10 ** 12  # kiloton to joules

    # following values can be changed to desired values
    rho_core = 18.71  # density of uranium core in gr/cm^3
    rho_tamper = 15.63  # density of WC tamper in gr/cm^3
    A_core = 235.04  # weight of core g/mol
    A_Tamper = 195.84  # weight of tamper g/mol
    sig_fission = 1.235  # cross section for fission in core in barns
    sig_elastic_core = 4.566  # cross section for elastic reaction in core in barns
    sig_elastic_tamper = 6.587  # cross section for elastic reaction in core in barns
    released_neutrons = 2.637  # average number of neutrons released during fission
    m_core = 64000  # mass of core in kg 64000 kg is default in little boy
    m_tamper = 552500  # mass of tamper in kg 552500 kg is default in little boy
    initial_compression = 1  # compression at start
    final_compression = 0.549927311 # final compression at k < 1

    # calculations for later use
    sig_core_total = sig_fission + sig_elastic_core
    n_core = rho_core * NA / A_core # nuclear number density core
    n_tamper = rho_tamper * NA / A_Tamper # nuclear number density tamper
    MFP_fission = 1 / (10 ** -24 * n_core * sig_fission)
    MFP_transport_core = 1 / (10 ** -24 * n_core * sig_core_total)
    MFP_transport_tamper = 1 / (10 ** -24 * n_core * sig_elastic_tamper)
    radius_start_core = ((3 * m_core) / (4 * pi * initial_compression * rho_core)) ** (1/3)
    radius_start_tamper = ((3 / (4 * pi)) * ((m_tamper / (initial_compression * rho_tamper)) + (m_core /
(initial_compression * rho_core)))) ** (1/3)
    d_core

