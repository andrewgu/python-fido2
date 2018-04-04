# Copyright (c) 2013 Yubico AB
# All rights reserved.
#
#   Redistribution and use in source and binary forms, with or
#   without modification, are permitted provided that the following
#   conditions are met:
#
#    1. Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#    2. Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


from __future__ import absolute_import, unicode_literals

from fido_host.ctap2 import AuthenticatorData
from fido_host.attestation import FidoU2FAttestation, PackedAttestation
from binascii import a2b_hex

import unittest


class TestAttestationObject(unittest.TestCase):
    def test_fido_u2f_attestation(self):
        FidoU2FAttestation().verify(
            {
                'sig': a2b_hex(b'30450220324779C68F3380288A1197B6095F7A6EB9B1B1C127F66AE12A99FE8532EC23B9022100E39516AC4D61EE64044D50B415A6A4D4D84BA6D895CB5AB7A1AA7D081DE341FA'),  # noqa
                'x5c': [a2b_hex(b'3082024A30820132A0030201020204046C8822300D06092A864886F70D01010B0500302E312C302A0603550403132359756269636F2055324620526F6F742043412053657269616C203435373230303633313020170D3134303830313030303030305A180F32303530303930343030303030305A302C312A302806035504030C2159756269636F205532462045452053657269616C203234393138323332343737303059301306072A8648CE3D020106082A8648CE3D030107034200043CCAB92CCB97287EE8E639437E21FCD6B6F165B2D5A3F3DB131D31C16B742BB476D8D1E99080EB546C9BBDF556E6210FD42785899E78CC589EBE310F6CDB9FF4A33B3039302206092B0601040182C40A020415312E332E362E312E342E312E34313438322E312E323013060B2B0601040182E51C020101040403020430300D06092A864886F70D01010B050003820101009F9B052248BC4CF42CC5991FCAABAC9B651BBE5BDCDC8EF0AD2C1C1FFB36D18715D42E78B249224F92C7E6E7A05C49F0E7E4C881BF2E94F45E4A21833D7456851D0F6C145A29540C874F3092C934B43D222B8962C0F410CEF1DB75892AF116B44A96F5D35ADEA3822FC7146F6004385BCB69B65C99E7EB6919786703C0D8CD41E8F75CCA44AA8AB725AD8E799FF3A8696A6F1B2656E631B1E40183C08FDA53FA4A8F85A05693944AE179A1339D002D15CABD810090EC722EF5DEF9965A371D415D624B68A2707CAD97BCDD1785AF97E258F33DF56A031AA0356D8E8D5EBCADC74E071636C6B110ACE5CC9B90DFEACAE640FF1BB0F1FE5DB4EFF7A95F060733F5')]  # noqa
            },
            AuthenticatorData(a2b_hex(b'1194228DA8FDBDEEFD261BD7B6595CFD70A50D70C6407BCF013DE96D4EFB17DE41000000000000000000000000000000000000000000403EBD89BF77EC509755EE9C2635EFAAAC7B2B9C5CEF1736C3717DA48534C8C6B654D7FF945F50B5CC4E78055BDD396B64F78DA2C5F96200CCD415CD08FE420038A5010203262001215820E87625896EE4E46DC032766E8087962F36DF9DFE8B567F3763015B1990A60E1422582027DE612D66418BDA1950581EBC5C8C1DAD710CB14C22F8C97045F4612FB20C91')),  # noqa
            a2b_hex(b'687134968222EC17202E42505F8ED2B16AE22F16BB05B88C25DB9E602645F141')  # noqa
        )

    def test_packed_attestation(self):
        PackedAttestation().verify(
            {
                'alg': -7,
                'sig': a2b_hex(b'304402204D49A9F9D58E2BDF8C20489BA318636422E4860048E391A105A408EBB556623F02201232B8F6CCA0A56F6654A1824B0E6F085DF2D7CF922F6F62A6B2F5F520D57EE6'),  # noqa
                'x5c': [a2b_hex(b'3082019330820138A003020102020900859B726CB24B4C29300A06082A8648CE3D0403023047310B300906035504061302555331143012060355040A0C0B59756269636F205465737431223020060355040B0C1941757468656E74696361746F72204174746573746174696F6E301E170D3136313230343131353530305A170D3236313230323131353530305A3047310B300906035504061302555331143012060355040A0C0B59756269636F205465737431223020060355040B0C1941757468656E74696361746F72204174746573746174696F6E3059301306072A8648CE3D020106082A8648CE3D03010703420004AD11EB0E8852E53AD5DFED86B41E6134A18EC4E1AF8F221A3C7D6E636C80EA13C3D504FF2E76211BB44525B196C44CB4849979CF6F896ECD2BB860DE1BF4376BA30D300B30090603551D1304023000300A06082A8648CE3D0403020349003046022100E9A39F1B03197525F7373E10CE77E78021731B94D0C03F3FDA1FD22DB3D030E7022100C4FAEC3445A820CF43129CDB00AABEFD9AE2D874F9C5D343CB2F113DA23723F3')]  # noqa
            },
            AuthenticatorData(a2b_hex(b'0021F5FC0B85CD22E60623BCD7D1CA48948909249B4776EB515154E57B66AE12410000002BF8A011F38C0A4D15800617111F9EDC7D0040A17370D9C1759005700C8DE77E7DFD3A0A5300E0A26E5213AA40D6DF10EE4028B58B5F34167035D840BEBAE0C5CE8FD05AD9BD33E3BE7D1C558D81AB4803570BA5010203262001215820A5FD5CE1B1C458C530A54FA61B31BF6B04BE8B97AFDE54DD8CBB69275A8A1BE1225820FA3A3231DD9DEED9D1897BE5A6228C59501E4BCD12975D3DFF730F01278EA61C')),  # noqa
            a2b_hex(b'11B8E5AA20AF76E2E9A6229E2D151480DC5B303130473205E69DD36AD742109C')  # noqa
        )