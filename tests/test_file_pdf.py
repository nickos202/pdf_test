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

    def test_key_coordinate(self):
        all_block_values = ReadPDF.read_pdf()
        Assertions.check_block_coordinates(all_block_values, ['GRIFFON AVIATION SERVICES LLC'], (6.005304336547852,
                                                                                                 17.99098777770996))
        Assertions.check_block_coordinates(all_block_values, ['PN', 'SN'], (13.511934280395508, 49.63319396972656))
        Assertions.check_block_coordinates(all_block_values, ['DESCRIPTION', 'LOCATION', 'CONDITION'],
                                           (13.511934280395508, 72.15308380126953))
        Assertions.check_block_coordinates(all_block_values, ['RECEIVER#', 'UOM'], (13.511934280395508,
                                                                                    83.41303253173828))
        Assertions.check_block_coordinates(all_block_values, ['EXP DATE', 'PO'], (13.511934280395508, 94.6729736328125))
        Assertions.check_block_coordinates(all_block_values, ['CERT SOURCE', ], (13.511934280395508, 105.93292236328125))
        Assertions.check_block_coordinates(all_block_values, ['REC.DATE', 'MFG'], (13.511934280395508, 117.19287109375))
        Assertions.check_block_coordinates(all_block_values, ['BATCH#', 'DOM'], (13.511934280395508, 128.45281982421875))
        Assertions.check_block_coordinates(all_block_values, ['REMARK', 'LOT#'], (13.511934280395508, 139.71275329589844))
        Assertions.check_block_coordinates(all_block_values, ['TAGGED BY'], (13.511934280395508, 150.9727020263672))
        # Assertions.check_block_coordinates(all_block_values, [], (86.32624816894531, 187.00453186035156))
        Assertions.check_block_coordinates(all_block_values, ['Qty'], (17.265249252319336, 195.26182556152344))
        Assertions.check_block_coordinates(all_block_values, ['NOTES'], (141.49998474121094, 150.9727020263672))
        Assertions.check_block_coordinates(all_block_values, ['inspection notes'], (146.00396728515625,
                                                                                    163.73397827148438))