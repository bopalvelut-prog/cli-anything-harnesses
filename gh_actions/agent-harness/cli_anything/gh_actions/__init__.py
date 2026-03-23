import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gh_actions running')
@cli.command()
def start(): click.echo('gh_actions started')
if __name__ == '__main__': cli()
