class DisableCSRF(object):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
        

#Al momento de realizar una carga de la web mediante implementacion a servidor debe de ser  comentado este archivo para obtener cookies de navegador