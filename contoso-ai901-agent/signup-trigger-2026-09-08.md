# Signup announcement in General

**Observed in the instructor tenant on September 8, 2026.** The existing automated flow,
**Contoso AI-901 - Announce certification signup**, now connects **Certification Signups** on
**Contoso HR Portal** to **Contoso Ltd Community > General**. This is the list created earlier
in this course preparation. For independent practice, select your own approved SharePoint list and Teams channel.

## Two nodes to teach

| Node | Configuration | Teaching point |
| --- | --- | --- |
| SharePoint: **When an item is created** | Site: Contoso HR Portal. List: Certification Signups. | Creating a row starts this independent automated flow. |
| Teams: **Post message in a chat or channel** | Post as: Flow bot. Post in: Channel. Team: Contoso Ltd Community. Channel: General. | Dynamic content carries the row's name, date, and record link into a useful notification. |

The message contains the heading **Contoso AI-901 certification signup**, the name, a readable
signup date, and **View signup in SharePoint**. It identifies the classroom demo and distinguishes
a signup from a verified exam pass or reward claim.

The list's visible **Name** field is its underlying `Title` column. Map that value to the message.
The date expression used in the saved action is:

```text
formatDateTime(triggerBody()?['SignupDate'], 'MMMM d, yyyy')
```

Use this expression to display the date consistently for the audience. The SharePoint record link
comes from the trigger's item link, so the announcement opens the row that caused this run.

## Trace the sequence

1. Open the list and the saved flow. Point out the two nodes and their selected resources.
2. Create one clearly labeled synthetic signup with today's date. Save it once.
3. Open the new flow run. Inspect the trigger's row and the Teams action's inputs and outputs.
4. Follow the returned Teams message link. Compare the name and date with the SharePoint row.
5. Explain that the coach can also create a row after fresh confirmation. Its returned signup
   result and this separate notification are two independently observable outcomes.

**Explain:** "The conversation collects confirmation and saves the signup. SharePoint then provides
the event for this separate flow. We inspect its run to prove that the announcement was posted."

The trigger checks for new items; notification arrival can lag behind the saved row. Each new row
produces a new announcement. Do not resubmit a successful run during rehearsal.

## Evidence actually observed

| Check | September 8 result |
| --- | --- |
| Saved destination | General in Contoso Ltd Community |
| Flow checker | **PASS**, zero errors and zero warnings |
| New synthetic item | Morgan Lee (Demo - General channel test), signup date September 8, 2026 |
| Trigger | **Succeeded** |
| Teams action | **Succeeded**, HTTP **201**, returned message link and the selected General channel identifier |
| Completion time | 7:18 AM Central |
| Coach consistency | Signup confirmation, instructions, and uploaded policy updated to name General; policy status Ready |
| Evaluation references | Three affected expected responses updated; evaluation sets **NOT RERUN** for this change |

This successful instructor test does not establish access to the demonstration tenant. Use your own
approved resources for independent practice; the names above identify the observed course example.

## Microsoft documentation

- [SharePoint connector reference](https://learn.microsoft.com/en-us/connectors/sharepointonline/)
- [Microsoft Teams connector reference](https://learn.microsoft.com/en-us/connectors/teams/)

The connector references were checked September 8, 2026. The configuration and outcomes above
come from the actual tenant test.
