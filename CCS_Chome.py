import winreg

def configure_chrome_settings_1():
    """
    Configura los ajustes de Chrome en el registro de Windows.
    Esta función aplica una serie de cambios en la configuración de Chrome
    en el registro de Windows. Se recomienda ejecutar esta función con privilegios
    de administrador para asegurarse de que los cambios se realicen correctamente.
    """
    try:
        ruta1 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Google\Chrome", 0, winreg.KEY_SET_VALUE)
    except Exception as e:
        print("Error al abrir la clave del registro:", e)
        return

    # se define una tupla 'cambios' con los valores que se debe realizar el cambio
    # en el registro de políticas de Windows para Chrome
    cambios = [
        # CAT I: el browser debe utilizar la version TLS 2.0 o superior
        ('SSLVersionMin', winreg.REG_SZ, 'tls1.2'),
        # CAT II: El cruce del cortafuegos desde el host remoto debe estar desactivado(0)
        ('RemoteAccessHostFirewallTraversal', winreg.REG_DWORD, 0x0),
        # CAT II: No permitir que ningún sitio rastree la ubicación del usuario(2)
        ('DefaultGeolocationSetting', winreg.REG_DWORD, 0x2),
        # CAT II: La capacidad de los sitios para mostrar ventanas emergentes debe estar deshabilitada.(2)
        ('DefaultPopupsSetting', winreg.REG_DWORD, 0x2),
        # CAT II: El browser debe realizar las búsquedas a sitios encriptados, es decir https(Google Encrypted)
        ('DefaultSearchProviderName', winreg.REG_SZ, 'Google Encrypted'),
        # CAT II: El proveedor de búsqueda predeterminado debe estar habilitado(1)
        ('DefaultSearchProviderEnabled', winreg.REG_DWORD, 0x1),
        # CAT II: El Administrador de contraseñas debe estar deshabilitado(0)
        ('PasswordManagerEnabled', winreg.REG_DWORD, 0x0),
        # CAT II: El procesamiento en segundo plano debe estar deshabilitado(0)
        ('BackgroundModeEnabled', winreg.REG_DWORD, 0x0),
        # CAT II: La sincronización de datos de Google debe estar deshabilitada(1)
        ('SyncDisabled', winreg.REG_DWORD, 0x1),
        # CAT II: El uso compartido de la impresión en la nube debe estar desactivado(0)
        ('CloudPrintProxyEnabled', winreg.REG_DWORD, 0x0),
        # CAT II: La predicción de red debe estar desactivada(2)
        ('NetworkPredictionOptions', winreg.REG_DWORD, 0x2),
        # CAT II: La notificación de métricas a Google debe estar desactivada(0)
        ('MetricsReportingEnabled', winreg.REG_DWORD, 0x0),
        # CAT II: Las sugerencias de búsqueda deben estar desactivadas(0)
        ('SearchSuggestEnabled', winreg.REG_DWORD, 0x0),
        # CAT II: La importación de contraseñas guardadas debe estar desactivada(0)
        ('ImportSavedPasswords', winreg.REG_DWORD, 0x0),
        # CAT II: El modo incógnito debe estar desactivado(1)
        ('IncognitoModeAvailability', winreg.REG_DWORD, 0x1),
        # CAT II: Deben realizarse comprobaciones de revocación en línea(1)
        ('EnableOnlineRevocationChecks', winreg.REG_DWORD, 0x1),
        # CAT II: La navegación segura debe estar activada(1)
        ('SafeBrowsingProtectionLevel', winreg.REG_DWORD, 0x1),
        # CAT II: El historial del navegador debe guardarse(0)
        ('SavingBrowserHistoryDisabled', winreg.REG_DWORD, 0x0),
        # CAT II: La eliminación del historial del navegador debe estar desactivada(0)
        ('AllowDeletingBrowserHistory', winreg.REG_DWORD, 0x0),
        # CAT II: La solicitud de ubicación de descarga debe estar activada(1)
        ('PromptForDownloadLocation', winreg.REG_DWORD, 0x1),
        # CAT II: Deben configurarse las restricciones de descarga(1)
        ('DownloadRestrictions', winreg.REG_DWORD, 0x1),
        # CAT II: El informe ampliado de navegación segura debe estar desactivado(0)
        ('SafeBrowsingExtendedReportingEnabled', winreg.REG_DWORD, 0x0),
        # CAT II: WebUSB debe estar desactivado(2)
        ('DefaultWebUsbGuardSetting', winreg.REG_DWORD, 0x2),
        # CAT II: Chrome Cleanup debe estar desactivado(0)
        ('ChromeCleanupEnabled', winreg.REG_DWORD, 0x0),
        # CAT II: El informe de limpieza de Chrome debe estar desactivado(0)
        ('ChromeCleanupReportingEnabled', winreg.REG_DWORD, 0x0),
        # CAT II: Google Cast debe estar desactivado(0)
        ('EnableMediaRouter', winreg.REG_DWORD, 0x0),
        # CAT II: La reproducción automática debe estar desactivada(0)
        ('AutoplayAllowed', winreg.REG_DWORD, 0x0),
        # CAT II: La recogida anónima de datos debe desactivarse(0)
        ('UrlKeyedAnonymizedDataCollectionEnabled', winreg.REG_DWORD, 0x0),
        # CAT II: La recopilación de registros de eventos WebRTC debe estar desactivada(0)
        ('WebRtcEventLogCollectionAllowed', winreg.REG_DWORD, 0x0),
        # CAT II: El Modo Invitado debe estar desactivado(0)
        ('BrowserGuestModeEnabled', winreg.REG_DWORD, 0x0),
        # CAT II: aucompletar para tarjeta de crédito debe de estar desabilitado(0)
        ('AutofillCreditCardEnabled', winreg.REG_DWORD, 0x0),
        # CAT II: aucompletar para direcciones debe de estar desabilitado(0)
        ('AutofillAddressEnabled', winreg.REG_DWORD, 0x0),
        # CAT II: Importar datos de formulario de Autorrelleno debe estar desactivado(0)
        ('ImportAutofillFormData', winreg.REG_DWORD, 0x0),
        # CAT II: El uso del protocolo QUIC debe estar desactivado(0)
        ('QuicAllowed', winreg.REG_DWORD, 0x0),
        # CAT II: Las herramientas de desarrollo de Chrome deben estar desactivadas(2)
        ('DeveloperToolsAvailability', winreg.REG_DWORD,0x2)
    ]

    # se realizan las escrituras de las políticas
    try:
        for subnombre, tipo, valor in cambios:
            winreg.SetValueEx(ruta1, subnombre, 0, tipo, valor)
    except Exception as e:
        print("Error al configurar la clave del registro:", e)

    # cierre de escritura
    winreg.CloseKey(ruta1)


def configure_chrome_settings_2():
    # Definir una lista de tuplas con las rutas, nombres y valores de las claves
    claves = [(r"SOFTWARE\Policies\Google\Chrome\ExtensionInstallBlocklist", "1", "*"),
              (r"SOFTWARE\Policies\Google\Chrome\ExtensionInstallAllowlist", "1", "oiigbmnaadbkfbmpbfijlflahbdbdgdf"),
              (r"SOFTWARE\Policies\Google\Chrome\URLBlocklist", "1", "javascript://*")]

    # un bucle for para iterar sobre las claves
    for ruta, nombre, valor in claves:
        # Usar un manejador de contexto para abrir y cerrar la clave automáticamente
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, ruta, 0, winreg.KEY_SET_VALUE) as clave:
            # se cambia el valor de la clave
            winreg.SetValueEx(clave, nombre, 0, winreg.REG_SZ, valor)


if __name__ == "__main__":
    configure_chrome_settings_1()
    configure_chrome_settings_2()
