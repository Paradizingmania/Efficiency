# created by Elias Axel Kærhøg
import math
# all values will be for little boy bomb with uranium core an Tungsten-carbide Tamper
# calculated using equations by Reed


def efficiency(mass_core, mass_tamper):

    if mass_core == 0:
        m_core = 64000  # mass of core in g 64000 g is default in little boy
    else:
        m_core = mass_core

    if mass_tamper == 0:
        m_tamper = 311000  # mass of tamper in g 311000 g is default in little boy
    else:
        m_tamper = mass_tamper

    # define constants for later use:
    NA = 6.022142 * 10 ** 23  # Avogadro's number
    pi = math.pi
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
    d_core = 1 / ( 1 ** -24 * n_core * sig_core_total)
    time_initial = (MFP_fission / v_neutron) / initial_compression

    # calculate values for critical threshold
    radius_final_core = ((3 * m_core)/(4 * pi * final_compression * rho_core)) ** (1/3)
    radius_final_tamper =(( 3 / (4 * pi)) * ((m_tamper / (final_compression * rho_tamper)) + (m_core /
(final_compression * rho_core)))) ** (1 / 3)
    d_final = d_core / final_compression
    MFP_tamper_final = MFP_transport_tamper / final_compression
    MFP = MFP_tamper_final / MFP_transport_core
    x = radius_final_core / d_final

    delta_Radius = radius_final_core - radius_start_core
    time_end = (MFP_fission / v_neutron) / final_compression
    Yield = ((m_core + m_tamper) / 8000) * ((0.01 * delta_Radius * (math.log(released_neutrons)) / time_end) ** 2) / kt
    eff = 100 * Yield / (17 * m_core/1000) # calculates efficiency of bomb

    return (Yield)






