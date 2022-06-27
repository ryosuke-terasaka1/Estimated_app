from app.domains.entities.ideal import IdealDataCreate


def get_ideal_data(dancer: IdealDataCreate):

    # この順番は固定させる
    dancer.Csv_data.columns = ["ボーカル", "メロディ", "ドラム"]

    dancer.Similarly_vocal = dancer.Csv_data['ボーカル']
    dancer.Similarly_melody = dancer.Csv_data['メロディ']
    dancer.Similarly_drum = dancer.Csv_data['ドラム']

    return dancer
