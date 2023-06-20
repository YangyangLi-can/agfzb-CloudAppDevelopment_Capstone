/**
 * Get all dealerships
 */

const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');

// async function main(params) {
//       const authenticator = new IamAuthenticator({ apikey: params.IAM_API_KEY })
//       const cloudant = CloudantV1.newInstance({
//           authenticator: authenticator
//       });
//       cloudant.setServiceUrl(params.COUCH_URL);
//       try {
//         let dbList = await cloudant.getAllDbs();
//         return { "dbs": dbList.result };
//       } catch (error) {
//           return { error: error.description };
//       }
// }
async function main(params) {
    const cloudant = Cloudant({
        url: params.COUCH_URL,
        plugins: { iamauth: { iamApiKey: params.IAM_API_KEY } }
    });


    try {
        let dbList = await cloudant.db.list();
        return { "dbs": dbList };
    } catch (error) {
        return { error: error.description };
    }
}
