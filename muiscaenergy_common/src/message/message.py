import pandas as pd

import pandas as pd

# Ejemplo de DataFrames df1 y df2 con las mismas columnas
data1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
data2 = {'A': [7, 8, 9], 'B': [10, 11, 12]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Apilar df2 sobre df1
stacked_df = pd.concat([df1, df2], ignore_index=True)

# stacked_df contiene ambos DataFrames apilados
print(stacked_df)

class Message:
    DT = 'datetime'
    DT_FROM = 'datetime_from'
    DT_TO = 'datetime_to'
    DT_UTC = 'datetime_utc'

    VAR = 'variable'
    VAL = 'value'

    COLUMNS = [DT_UTC, DT_FROM, DT_TO, VAR, VAL]


class TimeSeriesMessage(Message):

    def __init__(self):
        self.df = pd.DataFrame()

    def append_datetime(self, timeseries):
        self.df[Message.DT] = timeseries
        return self

    def append_datetime_utc(self, timeseries):
        self.df[Message.DT_UTC] = timeseries
        return self

    def append_datetime_from(self, timeseries):
        self.df[Message.DT_FROM] = timeseries
        return self

    def append_datetime_to(self, timeseries):
        self.df[Message.DT_TO] = timeseries
        return self

    def append(self, var, val):

        if len(var) == 1:
            self.df[Message.VAR] = var
            self.df[Message.VAL] = val

            return self

        temp_df = self.df.copy()
        for i, variable in enumerate(var):
            df_dummy = temp_df
            if i < 1:
                self.df[Message.VAR] = variable
                self.df[Message.VAL] = val[0]
                df_dummy = None
            else:
                df_dummy[Message.VAR] = variable
                df_dummy[Message.VAL] = val[i]

            self.df = pd.concat([self.df, df_dummy], ignore_index=True)

        return self


        #     for variable in var:
        #         self.df[Message.VAR] = variable
        #         self.df[Message.VAL] = val
        #
        #         self.df = pd.concat([self.df, self.df], ignore_index=True)

        # else:
        #     self.df = self.df.append(
        #         {Message.DT: self.df[Message.DT].iloc[-1], Message.DT_UTC: self.df[Message.DT_UTC].iloc[-1],
        #          Message.DT_FROM: self.df[Message.DT_FROM].iloc[-1], Message.DT_TO: self.df[Message.DT_TO].iloc[-1],
        #          Message.VAR: var, Message.VAL: val}, ignore_index=True)
        return self

        # self.df[Message.VARIABLE] = variable
        # self.df[Message.VALUE] = value
        # return self

    def append_value(self, value):
        self.df[Message.VAL] = value
        return self
