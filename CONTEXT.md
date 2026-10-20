# Shared vocabulary

**Corpus:** The collection of full reference documents retained for later evidence lookup. It is not a set of scan results.

**Ingestion:** Searching for reference material, extracting and normalizing its text, and retaining eligible documents. It does not execute security exercises.

**Search result:** A reference returned by a search provider. It is not a corpus document unless ingestion retains it.

**Document:** One retained reference with its full normalized text and source metadata. A document may contain multiple chunks.

**Chunk:** A contiguous character slice of a document's normalized text. Adjacent chunks may overlap; a chunk is not a token count, embedding or separate document.

**Topic:** The label grouping related search queries and identifying a document's ingestion context. It is not a workflow type.

**Query:** A search expression used to retrieve reference material for a topic. It is distinct from an exercise scenario.

**Preset:** A named collection of default ingestion settings. It is not a workflow plan or an executable exercise.

**Domain:** The registrable domain of a source URL, including its public suffix. It is not the exact hostname or an authorized target boundary.

**Workflow plan:** A structured exercise plan for human review, containing phases, assumptions, a scorecard and optional evidence sources. Generating one does not execute its actions.
Avoid: executed workflow; scan result.

**Workflow type:** The red, blue or purple category selecting the plan's fixed phase template: adversary-oriented, defensive or joint-team planning respectively.

**Workflow phase:** One named part of a workflow plan, with an objective, suggested actions and expected outputs. Its presence does not mean those actions ran or outputs exist.

**Scenario:** The exercise description used to frame a workflow plan and find supporting reference material. It is not an execution request.

**Scope:** A label included in workflow-plan output, such as lab or staging. It neither authorizes actions nor enforces an execution boundary.
Avoid: execution scope when describing the CLI label.

**Evidence source:** A reference attached to a workflow plan, with identifying metadata and a short excerpt. It is a citation, not proof that an exercise ran or a vulnerability exists.
Avoid: verified finding; scan evidence.

**Estimated spend cap:** A threshold for estimated ingestion spending, evaluated after search results are returned. It is not a hard provider billing limit.
