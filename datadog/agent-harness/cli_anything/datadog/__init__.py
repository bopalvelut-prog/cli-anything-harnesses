import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def agent(): click.echo('Datadog agent running')
@cli.command()
def check(): subprocess.run(['datadog-agent', 'status'])
@cli.command()
def install(): click.echo('Datadog installed')
if __name__ == '__main__': cli()
