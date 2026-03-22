import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('domain')
def check(domain): subprocess.run(['echo | openssl s_client -connect ' + domain + ':443'], shell=True)
if __name__ == '__main__': cli()
