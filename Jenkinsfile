pipeline {
    agent any 
    stages {
        stage('copyfiles') {
            steps {
                    
                    sh '''#!/bin/bash
                    tar -cvf pipeline.tar *
                    aws s3 cp pipeline.tar s3://codebucketinstall/
                    aws deploy create-deployment --application-name demo --deployment-group-name grp --deployment-config-name CodeDeployDefault.OneAtATime --s3-location "bucket=codebucketinstall,key=pipeline.tar,bundleType=tar"
                    '''

            }
        }
    }
}
