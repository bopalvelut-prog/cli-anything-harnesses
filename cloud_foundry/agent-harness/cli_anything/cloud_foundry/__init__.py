import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cloud_foundry running')
@cli.command()
def start(): click.echo('cloud_foundry started')
if __name__ == '__main__': cli()
