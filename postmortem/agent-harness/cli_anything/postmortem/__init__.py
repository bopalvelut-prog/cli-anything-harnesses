import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('postmortem running')
@cli.command()
def start(): click.echo('postmortem started')
if __name__ == '__main__': cli()
