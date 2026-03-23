import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('seata running')
@cli.command()
def start(): click.echo('seata started')
if __name__ == '__main__': cli()
