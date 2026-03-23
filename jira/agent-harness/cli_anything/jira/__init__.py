import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jira running')
@cli.command()
def start(): click.echo('jira started')
if __name__ == '__main__': cli()
