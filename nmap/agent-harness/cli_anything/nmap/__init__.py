import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('target')
def scan(target): subprocess.run(['nmap', '-sV', target])
@cli.command()
@click.argument('target')
def os_detect(target): subprocess.run(['nmap', '-O', target])
@cli.command()
@click.argument('file')
def scan_list(file): subprocess.run(['nmap', '-iL', file])
if __name__ == '__main__': cli()
