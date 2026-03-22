import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def tickets(): click.echo('Zendesk tickets')
@cli.command()
def users(): click.echo('Zendesk users')
if __name__ == '__main__': cli()
