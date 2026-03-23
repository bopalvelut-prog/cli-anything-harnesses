import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tokio running')
@cli.command()
def start(): click.echo('tokio started')
if __name__ == '__main__': cli()
