import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('New Relic agent running')
@cli.command()
def diagnose(): subprocess.run(['newrelic-cli', 'diagnose'])
if __name__ == '__main__': cli()
