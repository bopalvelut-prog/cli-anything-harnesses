import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('submit running')
@cli.command()
def start(): click.echo('submit started')
if __name__ == '__main__': cli()
