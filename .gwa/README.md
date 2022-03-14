# Setup

We have a `UI` (aps-ref.apps.gov.bc.ca) that is protected by `oidc` and therefore forces login, and establishes a session cookie.

We have an `API` (aps-ref-api-gov-bc-ca.dev.api.gov.bc.ca) that is protected with `jwt-keycloak` and the `kong-upstream-jwt`.

When the `UI` calls the `API`, it passes the Token used for login by the UI. The `azp` is the UI.

`PKCE` support in the `oidc` plugin?
`Audience validation` support in the `jwt-keycloak` plugin - or can we just use `oidc`?

Perhaps it is better practice to have the UI proxy the API so that it does not need to worry about session management and holding the Token

## Publishing

```
gwa publish issuer -b issuer.yaml
gwa publish dataset -b dataset.yaml
gwa publish product -b product.yaml
gwa publish product -b product2.yaml

gwa pg gateway.yaml
```

> NOTE: Required extra permissions (perm-domains) and (perm-protected-ns)
> NOTE: Product didn't import with active existing - Access Denied
> NOTE: Issuer once created was not able to be updated because Service Account did not own the Credential Issuer record
> NOTE: For the API and Client Credential Flow, should it be a different Credential Issuer?
> NOTE: Environment re-assigned which caused My Access to fail
