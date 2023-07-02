from read.readPDF import ReadPDF
from assertion.assertions import Assertions


class Test_PDF:


    def test_key_blocks_pdf(self):
        all_block_values = ReadPDF.read_pdf()
        Assertions.check_block_key(all_block_values, ['GRIFFON AVIATION SERVICES LLC'])
        Assertions.check_block_key(all_block_values, ['PN'])
        Assertions.check_block_key(all_block_values, ['SN'])
        Assertions.check_block_key(all_block_values, ['DESCRIPTION'])
        Assertions.check_block_key(all_block_values, ['LOCATION'])
        Assertions.check_block_key(all_block_values, ['CONDITION'])
        Assertions.check_block_key(all_block_values, ['RECEIVER#'])
        Assertions.check_block_key(all_block_values, ['UOM'])
        Assertions.check_block_key(all_block_values, ['EXP DATE'])
        Assertions.check_block_key(all_block_values, ['PO'])
        Assertions.check_block_key(all_block_values, ['CERT SOURCE'])
        Assertions.check_block_key(all_block_values, ['REC.DATE'])
        Assertions.check_block_key(all_block_values, ['MFG'])
        Assertions.check_block_key(all_block_values, ['BATCH#'])
        Assertions.check_block_key(all_block_values, ['DOM'])
        Assertions.check_block_key(all_block_values, ['REMARK'])
        Assertions.check_block_key(all_block_values, ['LOT#'])
        Assertions.check_block_key(all_block_values, ['TAGGED BY'])
        Assertions.check_block_key(all_block_values, ['Qty'])
        Assertions.check_block_key(all_block_values, ['NOTES'])
        Assertions.check_block_key(all_block_values, ['inspection notes'])

    def test_key_line(self):
        all_block_values = ReadPDF.read_pdf()
        Assertions.check_block_coordinates(all_block_values, ['GRIFFON AVIATION SERVICES LLC'], 6.005304336547852)
        Assertions.check_block_coordinates(all_block_values, ['PN', 'SN'], 13.511934280395508)
        Assertions.check_block_coordinates(all_block_values, ['DESCRIPTION', 'LOCATION', 'CONDITION'],
                                           13.511934280395508)
        Assertions.check_block_coordinates(all_block_values, ['RECEIVER#', 'UOM'], 13.511934280395508)
        Assertions.check_block_coordinates(all_block_values, ['EXP DATE', 'PO'], 13.511934280395508)
        Assertions.check_block_coordinates(all_block_values, ['CERT SOURCE', ], 13.511934280395508)
        Assertions.check_block_coordinates(all_block_values, ['REC.DATE', 'MFG'], 13.511934280395508)
        Assertions.check_block_coordinates(all_block_values, ['BATCH#', 'DOM'], 13.511934280395508)
        Assertions.check_block_coordinates(all_block_values, ['REMARK', 'LOT#'], 13.511934280395508)
        Assertions.check_block_coordinates(all_block_values, ['TAGGED BY'], 13.511934280395508)
        # Assertions.check_block_coordinates(all_block_values, [], 86.32624816894531)
        Assertions.check_block_coordinates(all_block_values, ['Qty'], 17.265249252319336)
        Assertions.check_block_coordinates(all_block_values, ['NOTES'], 141.49998474121094)
        Assertions.check_block_coordinates(all_block_values, ['inspection notes'], 146.00396728515625)