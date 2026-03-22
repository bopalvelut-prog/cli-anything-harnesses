import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def contacts(): click.echo('ActiveCampaign contacts')
@cli.command()
def campaigns(): click.echo('ActiveCampaign campaigns')
if __name__ == '__main__': cli()
