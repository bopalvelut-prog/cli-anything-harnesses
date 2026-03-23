import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('github_pages running')
@cli.command()
def start(): click.echo('github_pages started')
if __name__ == '__main__': cli()
