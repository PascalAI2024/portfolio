# ButlerCRM — from customer context to delivered work

I built ButlerCRM with Elixir, Phoenix LiveView and PostgreSQL to connect
customer relationships, projects and the work a team needs to deliver.

The screenshots below show the actual application running locally with
fictional demo records, captured September 5, 2026. The production source
is private.

## Keep the customer relationship in context

The customer record brings identity, status, activity history and linked
opportunities into one view. This fictional example connects a discovery
note with its related website opportunity.

![Actual ButlerCRM customer record with activity timeline and linked sales opportunity](../assets/butlercrm/customer-desktop.jpg)

The sales pipeline groups opportunities by stage. Here, five fictional
opportunities sit across discovery, proposal, review and confirmation. Deal
values are unpopulated; the displayed totals are not sales results.

![Actual ButlerCRM sales pipeline with four stages and five fictional opportunities](../assets/butlercrm/pipeline-desktop-v2.jpg)

<img src="../assets/butlercrm/customer-mobile.jpg" alt="Actual customer timeline and linked opportunity on a mobile screen" width="420" />

## Make the next step visible

A project board gives work a clear path from brief to build, review and
delivery. Tasks remain visible in their current stage, with priority labels
and stage counts that make it easier to see what needs attention.

![ButlerCRM application board with four stages and seven fictional demo tasks](../assets/butlercrm/butler-board-desktop.jpg)

## Keep the detail with the task

Opening a task preserves the surrounding project context. Its description,
subtasks, related records, time tracking, attachments and conversation share
one detail view. The example shows a review task with a subtask and a comment.

![Actual ButlerCRM task detail showing subtasks, time tracking and comments](../assets/butlercrm/butler-task-detail.jpg)

## Carry the workflow onto a smaller screen

The task detail adapts to a narrow viewport while retaining the same work
record and controls. This keeps the desktop and mobile experience connected.

<img src="../assets/butlercrm/butler-task-mobile-420.jpg" alt="ButlerCRM task detail at a narrow mobile viewport, using fictional demo records" width="390" />

## Engineering approach

Phoenix LiveView keeps the interface tied to application state, backed by
PostgreSQL. The work board is part of the wider CRM application shell, alongside
project navigation, collaboration and administration.

[Capture provenance](../assets/butlercrm/README.md) describes the isolated
demo environment and what these examples establish.
