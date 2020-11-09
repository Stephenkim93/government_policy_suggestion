doc1_check_field1_words = ['대졸']
doc1_check_field2_words = ['컴공']

doc2_check_field1_words = ['대졸']
doc2_check_field2_words = ['경영']

def makeCheckWordIndex(totalDocCheckFieldAndWordInfo, saveJsonFileName):
    # [
    #     {
    #         'fieldName': '학력',
    #         'indexingInfo': [
    #             {
    #                 'checkWord': "대졸",
    #                 "DocIDList": ['doc1', 'doc2']
    #             }
    #         ]
    #     },
    #     {
    #         'fieldName': '전공',
    #         'indexingInfo': [
    #             {
    #                 'checkWord': "컴공",
    #                 "DocIDList": ['doc1']
    #             },
    #             {
    #                 'checkWord': "경영",
    #                 "DocIDList": ['doc2']
    #             }
    #         ]
    #     }
    # ]

    pass