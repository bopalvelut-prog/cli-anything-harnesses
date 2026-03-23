import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gvisor running')
@cli.command()
def start(): click.echo('gvisor started')
if __name__ == '__main__': cli()
