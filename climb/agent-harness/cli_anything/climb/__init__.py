import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('climb running')
@cli.command()
def start(): click.echo('climb started')
if __name__ == '__main__': cli()
