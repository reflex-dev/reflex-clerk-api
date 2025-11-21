# Reflex Clerk API Documentation

Welcome to the Reflex Clerk API documentation! This package provides integration with the [Clerk](https://clerk.com) authentication service, allowing you to easily manage user authentication within within your [Reflex](https://reflex.dev) app.

## Overview

Primarily, this package wraps the [@clerk/clerk-react](https://www.npmjs.com/package/@clerk/clerk-react) library, using the Clerk maintained [clerk-backend-api](https://pypi.org/project/clerk-backend-api/") python package to synchronize the reflex FastAPI backend with the Clerk frontend components.

### Wrapped Components

An overview of some of the clerk-react components that are wrapped here:

- **ClerkProvider**: A component that wraps your app/page to handle Clerk authentication.
- **Control Components**: Components such as `clerk_loaded`, `protect`, and `signed_in`, etc.
- **Authentication Components**: Components for `sign_in` and `sign_up` that redirect the user to Clerk's authentication pages.
- **Wrapper Components**: Button wrappers for `sign_in_button`, `sign_out_button`, and `user_button`, that you can wrap regular reflex components with.

See more in the [features](features.md) section.

### Backend synchronization

The `ClerkProvider` state is set up so that the backend states are synchronized with the Clerk authentication that happens in the frontend. The two main reflex backend states are:

- **ClerkState**: Manages the authentication state of the user.
- **ClerkUser**: Optional state for accessing additional user information.

Additionally, you can keep your own states up to date by registering event handlers to be called on authentication changes with e.g. `clerk.register_on_auth_change_handler(State.some_handler)`.

### Additional Notes

This packages:

- Is fully asynchronous, using `async/await` for all requests to the Clerk backend.
- Supports Reflex 0.7.x.
- Provides helper functions for handling `on_load` events that require knowledge of user authentication status.
- Allows registration of event handlers to be called on authentication changes (login/logout).
- Is fully typed
- Is tested against python versions 3.11 - 3.13

## Demo

See a demo of `reflex-clerk-api` [here](https://reflex-clerk-api-demo.adventuresoftim.com).

The demo uses a development Clerk account so you can try out sign-up/sign-in etc.

## Quick Links

Additionally, you can find the following resources in the documentation:

- [Getting Started](getting_started.md): Learn how to install and set up the Reflex Clerk API.
- [Migration Guide](migrating.md): Notes on migrating from the `Kroo/reflex-clerk` package.
- [Features](features.md): More details on the additional features provided.

## Not yet implemented

Some of these things are minimally implemented, but not at all tested, and likely without the additional props.

- **GoogleOneTap**
- **Waitlist**
- **Organization Components**
