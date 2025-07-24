from typing import Optional
from reflex_clerk_api.base import ClerkBase


class CreateOrganization(ClerkBase):
    """
    The CreateOrganization component provides a form for users to create new organizations.

    This component renders Clerk's <CreateOrganization /> React component,
    allowing users to set up new organizations with customizable appearance and routing.

    Props:
        appearance: Optional object to style your components. Will only affect Clerk components.
        path: The path where the component is mounted when routing is set to 'path'.
        routing: The routing strategy for your pages. Defaults to 'path' for frameworks
                that handle routing, or 'hash' for other SDKs.
        after_create_organization_url: The full URL or path to navigate to after creating an organization.
        fallback: An optional element to be rendered while the component is mounting.
    """

    tag = "CreateOrganization"

    # Optional props that CreateOrganization supports
    appearance: Optional[str] = None
    path: Optional[str] = None
    routing: Optional[str] = None
    after_create_organization_url: Optional[str] = None
    fallback: Optional[str] = None


class OrganizationProfile(ClerkBase):
    """
    The OrganizationProfile component allows users to manage their organization membership and security settings.

    This component renders Clerk's <OrganizationProfile /> React component,
    allowing users to manage organization information, members, billing, and security settings.

    Props:
        appearance: Optional object to style your components. Will only affect Clerk components.
        path: The path where the component is mounted when routing is set to 'path'.
        routing: The routing strategy for your pages. Defaults to 'path' for frameworks
                that handle routing, or 'hash' for other SDKs.
        after_leave_organization_url: The full URL or path to navigate to after leaving an organization.
        custom_pages: An array of custom pages to add to the organization profile.
        fallback: An optional element to be rendered while the component is mounting.
    """

    tag = "OrganizationProfile"

    # Optional props that OrganizationProfile supports
    appearance: Optional[str] = None
    path: Optional[str] = None
    routing: Optional[str] = None
    after_leave_organization_url: Optional[str] = None
    custom_pages: Optional[str] = None
    fallback: Optional[str] = None


class OrganizationSwitcher(ClerkBase):
    """
    The OrganizationSwitcher component displays the currently active organization and allows users to switch between organizations.

    This component renders Clerk's <OrganizationSwitcher /> React component,
    providing a dropdown interface for organization switching with customizable appearance.

    Props:
        appearance: Optional object to style your components. Will only affect Clerk components.
        organization_profile_mode: Controls whether selecting the organization opens as a modal or navigates to a page.
        organization_profile_url: The full URL or path leading to the organization management interface.
        create_organization_mode: Controls whether selecting create organization opens as a modal or navigates to a page.
        create_organization_url: The full URL or path leading to the create organization interface.
        after_leave_organization_url: The full URL or path to navigate to after leaving an organization.
        after_create_organization_url: The full URL or path to navigate to after creating an organization.
        after_select_organization_url: The full URL or path to navigate to after selecting an organization.
        default_open: Controls whether the OrganizationSwitcher should open by default during the first render.
        hide_personal_account: Controls whether the personal account option is hidden in the switcher.
        fallback: An optional element to be rendered while the component is mounting.
    """

    tag = "OrganizationSwitcher"

    # Optional props that OrganizationSwitcher supports
    appearance: Optional[str] = None
    organization_profile_mode: Optional[str] = None
    organization_profile_url: Optional[str] = None
    create_organization_mode: Optional[str] = None
    create_organization_url: Optional[str] = None
    after_leave_organization_url: Optional[str] = None
    after_create_organization_url: Optional[str] = None
    after_select_organization_url: Optional[str] = None
    default_open: Optional[str] = None
    hide_personal_account: Optional[str] = None
    fallback: Optional[str] = None


class OrganizationList(ClerkBase):
    """
    The OrganizationList component displays a list of organizations that the user is a member of.

    This component renders Clerk's <OrganizationList /> React component,
    providing an interface to view and manage organization memberships.

    Props:
        appearance: Optional object to style your components. Will only affect Clerk components.
        after_create_organization_url: The full URL or path to navigate to after creating an organization.
        after_select_organization_url: The full URL or path to navigate to after selecting an organization.
        after_select_personal_url: The full URL or path to navigate to after selecting the personal account.
        create_organization_mode: Controls whether selecting create organization opens as a modal or navigates to a page.
        create_organization_url: The full URL or path leading to the create organization interface.
        hide_personal_account: Controls whether the personal account option is hidden in the list.
        skip_invitation_screen: Controls whether to skip the invitation screen when creating an organization.
        fallback: An optional element to be rendered while the component is mounting.
    """

    tag = "OrganizationList"

    # Optional props that OrganizationList supports
    appearance: Optional[str] = None
    after_create_organization_url: Optional[str] = None
    after_select_organization_url: Optional[str] = None
    after_select_personal_url: Optional[str] = None
    create_organization_mode: Optional[str] = None
    create_organization_url: Optional[str] = None
    hide_personal_account: Optional[str] = None
    skip_invitation_screen: Optional[str] = None
    fallback: Optional[str] = None


create_organization = CreateOrganization.create
organization_profile = OrganizationProfile.create
organization_switcher = OrganizationSwitcher.create
organization_list = OrganizationList.create
