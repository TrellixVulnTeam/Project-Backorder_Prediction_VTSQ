from backorder.pipeline.pipeline import Pipeline
from backorder.exception import BackorderPredictionException
from backorder.logger import logging
from backorder.config.configuration import Configuartion
from backorder.component.data_transformation import DataTransformation
import os


def main():
    try:
        config_path = os.path.join("config", "config.yaml")
        pipeline = Pipeline(Configuartion(config_file_path=config_path))
        #pipeline.run_pipeline()
        pipeline.start()
        logging.info("main function execution completed.")
        # # data_validation_config = Configuartion().get_data_transformation_config()
        # # print(data_validation_config)
        # schema_file_path=r"D:\Project\machine_learning_project\config\schema.yaml"
        # file_path=r"D:\Project\machine_learning_project\housing\artifact\data_ingestion\2022-06-27-19-13-17\ingested_data\train\housing.csv"

        # df= DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        # print(df.columns)
        # print(df.dtypes)

    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()

