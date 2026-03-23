import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('real running')
@cli.command()
def start(): click.echo('real started')
if __name__ == '__main__': cli()
