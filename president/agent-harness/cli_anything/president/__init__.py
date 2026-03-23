import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('president running')
@cli.command()
def start(): click.echo('president started')
if __name__ == '__main__': cli()
