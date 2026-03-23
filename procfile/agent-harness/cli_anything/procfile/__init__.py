import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('procfile running')
@cli.command()
def start(): click.echo('procfile started')
if __name__ == '__main__': cli()
