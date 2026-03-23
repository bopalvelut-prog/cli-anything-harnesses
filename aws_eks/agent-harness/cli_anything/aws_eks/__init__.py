import click
@click.group()
def cli(): pass
@cli.command()
def clusters(): click.echo('EKS clusters')
@cli.command()
def nodes(): click.echo('EKS nodes')
if __name__ == '__main__': cli()
