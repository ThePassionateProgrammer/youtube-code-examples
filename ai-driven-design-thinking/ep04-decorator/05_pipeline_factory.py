class PipelineFactory:
    def create(self, mode):
        if mode == "secure":
            return Pipeline([
                ValidateStep(),
                EncryptStep(),
                LogStep()
            ])