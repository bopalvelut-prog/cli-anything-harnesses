import click
@click.group()
def cli(): pass
@cli.command()
def instances(): click.echo('RDS instances')
@cli.command()
def snapshots(): click.echo('RDS snapshots')
if __name__ == '__main__': cli()
