# Copyright Elasticsearch B.V. and/or licensed to Elasticsearch B.V. under one
# or more contributor license agreements. Licensed under the Elastic License
# 2.0; you may not use this file except in compliance with the Elastic License
# 2.0.

import pytest

from detection_rules.misc import get_default_config

from tests.conftest import TestBaseRule

# from detection_rules.remote_validation import RemoteValidator


@pytest.mark.skipif(get_default_config() is None, reason='Skipping remote validation due to missing config')
class TestRemoteRules(TestBaseRule):
    """Test rules against a remote Elastic stack instance."""

    # def test_esql_rules(self):
    #    """Temporarily explicitly test all ES|QL rules remotely pending parsing lib."""
    #    esql_rules = [r for r in self.all_rules if r.contents.data.type == 'esql']
    #    rv = RemoteValidator(parse_config=True)
    #    rv.validate_rules(esql_rules)
