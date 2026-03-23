import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('appwrite running')
@cli.command()
def start(): click.echo('appwrite started')
if __name__ == '__main__': cli()
