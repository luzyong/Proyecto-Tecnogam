from pylogix import PLC
def scada():
    with PLC() as comm:
        comm.IPAddress = '192.168.1.9'
        SH_TempZ1 = comm.Read('SH_TempZ1')
        SH_TempZ2 = comm.Read('SH_TempZ2')
        SH_TempCHMY_1 = comm.Read('SH_TempCHMY_1')
        SH_TempCHMY_2 = comm.Read('SH_TempCHMY_2')
        SH_SP_TempZ1 = comm.Read('SH_SP_TempZ1')
        SH_SP_TempZ2 = comm.Read('SH_SP_TempZ2')
        SH_SP_TempCHMYZ1 = comm.Read('SH_SP_TempCHMYZ1')
        SH_SP_TempCHMYZ2 = comm.Read('SH_SP_TempCHMYZ2')
        SH_Lim_TempZ1 = comm.Read('SH_Lim_TempZ1')
        SH_Lim_TempZ2 = comm.Read('SH_Lim_TempZ2')
        SH_Num_Lote_Actual = comm.Read('SH_Num_Lote_Actual')
        SH_Tipo_Material_Actual = comm.Read('SH_Tipo_Material_Actual')
        SH_Cant_Material_Actual = comm.Read('SH_Cant_Material_Actual ')
        SH_PB_enc_Extractor = comm.Read('SH_PB_enc_Extractor')
        SH_PB_enc_Bomba = comm.Read('SH_PB_enc_Bomba')
        SH_PB_enc_Turbo1 = comm.Read('SH_PB_enc_Turbo1')
        SH_PB_enc_Turbo2 = comm.Read('SH_PB_enc_Turbo2')
        SH_PB_enc_Quemador = comm.Read('SH_PB_enc_Quemador')
        SH_PB_Abrir_Puerta = comm.Read('SH_PB_Abrir_Puerta')
        SH_PB_apag_Extractor = comm.Read('SH_PB_apag_Extractor')
        SH_PB_apag_Bomba = comm.Read('SH_PB_apag_Bomba')
        SH_PB_apag_Turbo1 = comm.Read('SH_PB_apag_Turbo1')
        SH_PB_apag_Turbo2 = comm.Read('SH_PB_apag_Turbo2')
        SH_PB_apag_Quemador = comm.Read('SH_PB_apag_Quemador')
        SH_PB_Cerrar_Puerta = comm.Read('SH_PB_Cerrar_Puerta')
        SH_Falla_Motor = comm.Read('SH_Falla_Motor')
        SH_Falla_Temperatura = comm.Read('SH_Falla_Temperatura')
        SH_Falla_Quemador = comm.Read('SH_Falla_Quemador')
        #print(ret.TagName, ret.Value, ret.Status)
        valores = [SH_TempZ1.Value,SH_TempZ1.Value,SH_TempZ2.Value,SH_TempCHMY_1.Value,SH_TempCHMY_2.Value,SH_SP_TempZ1.Value,SH_SP_TempZ2.Value,SH_SP_TempCHMYZ1.Value,SH_SP_TempCHMYZ2.Value,
        SH_Lim_TempZ1.Value,SH_Lim_TempZ2.Value,SH_Num_Lote_Actual.Value,SH_Tipo_Material_Actual.Value,SH_Cant_Material_Actual.Value,SH_PB_enc_Extractor.Value,SH_PB_enc_Bomba.Value,
        SH_PB_enc_Turbo1.Value,SH_PB_enc_Turbo2.Value,SH_PB_enc_Quemador.Value,SH_PB_Abrir_Puerta.Value,SH_PB_apag_Extractor.Value,SH_PB_apag_Bomba.Value,SH_PB_apag_Turbo1.Value,
        SH_PB_apag_Turbo2.Value,SH_PB_apag_Quemador.Value,SH_PB_Cerrar_Puerta.Value,SH_Falla_Motor.Value,SH_Falla_Temperatura.Value,SH_Falla_Quemador.Value]     
         
        return valores 

