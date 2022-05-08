# write your program here
import string


def replace_sequence(sequence):
    replacements = {"A": "T",
                    "T": "A",
                    "G": "C",
                    "C": "G"}
    return sequence.translate(str.maketrans(replacements))


def separate_dna_strands(strand_string):
    return strand_string.split(" ")


def separator_nucleotide_position(separator):
    if separator.find("CT") > -1:
        return separator.find("CT")
    return separator.find("TC")


def perform_strand_operation(strand_string):
    dna_strands = separate_dna_strands(strand_string)
    separator = "CTGCAG"
    print(cut_first_nucleotides(dna_strands[0], separator))
    print(cut_inverted_nucleotides(dna_strands[1], separator))


def reverse_separator(separator):
    return separator[::-1]


def cut_first_nucleotides(dna_strand, separator):
    if dna_strand.find(separator) > -1:
        num = dna_strand.find(separator) + 1

    return dna_strand[:num] + " " + dna_strand[num:]


def cut_inverted_nucleotides(dna_strand, separator):
    if dna_strand.rfind(reverse_separator(separator)) > -1:
        num = dna_strand.rfind(reverse_separator(separator)) + len(separator) - 1

    return dna_strand[:num] + " " + dna_strand[num:]


def original_complementary_strand(dna_strand):
    print(dna_strand)
    print(replace_sequence(dna_strand))


def separate_restriction_sites(restriction_sites):
    return restriction_sites.split(" ")


def extract_gfp_chains(dna_strand, restriction_sites):
    restriction_site_1, restriction_site_2 = separate_restriction_sites(restriction_sites)
    pos_1 = dna_strand.find(restriction_site_1) + 1
    pos_2 = dna_strand.rfind(restriction_site_2) + 1
    pos_3 = dna_strand.find(restriction_site_1[::-1]) + len(restriction_site_1) - 1
    pos_4 = dna_strand.rfind(restriction_site_2[::-1]) + len(restriction_site_2) - 1
    print(pos_3, pos_4)
    return [dna_strand[pos_1:pos_2],
            dna_strand[pos_3:pos_4]]


def ends_that_stick(dna_strand, restriction_sites):
    return_template = string.Template("$gfp\n$gfp2")
    print(extract_gfp_chains(dna_strand, restriction_sites))
    gfp, gfp2 = extract_gfp_chains(dna_strand, restriction_sites)
    print(return_template.substitute(gfp=gfp,
                                     gfp2=gfp2))


strand = input()
sites = input()
ends_that_stick(strand, sites)
