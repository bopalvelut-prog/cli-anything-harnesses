import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('freshrss running')
@cli.command()
def start(): click.echo('freshrss started')
if __name__ == '__main__': cli()
